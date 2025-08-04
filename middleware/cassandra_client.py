# middleware/cassandra_client.py
from cassandra.cluster import Cluster
from cassandra.policies import TokenAwarePolicy, RoundRobinPolicy
from concurrent.futures import ThreadPoolExecutor, as_completed

from middleware.node_selector import select_target_nodes_under_threshold
from middleware.utils import load_config

config = load_config()


def build_query(op: dict) -> str:
    op_type = op.get("operation")
    table = "user_network_topology.ycsb"

    if op_type == "INSERT":
        fields = [f"field{i}" for i in range(10)]
        columns = ["y_id"] + fields
        values = [f"'{op['y_id']}'"] + [f"'{op.get(f, '')}'" for f in fields]
        query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(values)});"

    elif op_type == "READ":
        query = f"SELECT * FROM {table} WHERE y_id = '{op['y_id']}';"

    elif op_type == "UPDATE":
        set_clause = ", ".join([f"{f} = '{op.get(f, '')}'" for f in [f"field{i}" for i in range(10)]])
        query = f"UPDATE {table} SET {set_clause} WHERE y_id = '{op['y_id']}';"

    elif op_type == "DELETE":
        query = f"DELETE FROM {table} WHERE y_id = '{op['y_id']}';"

    else:
        raise ValueError(f"Unsupported operation type: {op_type}")

    return query


def execute_on_node(node_ip: str, query: str):
    cluster = Cluster([node_ip], load_balancing_policy=TokenAwarePolicy(RoundRobinPolicy()))
    session = cluster.connect('user_network_topology')
    result = session.execute(query)
    cluster.shutdown()
    return result


def forward_to_cassandra(op: dict, consistency_type: str):
    query = build_query(op)
    eligible_nodes = select_target_nodes_under_threshold(threshold=20)  # Adjustable threshold

    results = []
    if not eligible_nodes:
        return {"status": "failed", "reason": "No nodes under load threshold"}

    with ThreadPoolExecutor(max_workers=len(eligible_nodes)) as executor:
        futures = {executor.submit(execute_on_node, ip, query): ip for ip in eligible_nodes}

        for future in as_completed(futures):
            node_ip = futures[future]
            try:
                result = future.result()
                results.append({"node": node_ip, "status": "executed"})
            except Exception as e:
                results.append({"node": node_ip, "status": "error", "message": str(e)})

    return {
        "status": "distributed_execution",
        "consistency": consistency_type,
        "executions": results
    }
