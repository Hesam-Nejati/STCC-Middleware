# default_one.py
import subprocess
from node_selector import select_target_nodes_under_threshold

CONSISTENCY = "ONE"
WORKLOAD_PATH = "YCSB/workloads/workloadc"
YCSB_PATH = "YCSB"
TABLE = "user_network_topology.ycsb"

if __name__ == "__main__":
    nodes = select_target_nodes_under_threshold(threshold=20)
    if not nodes:
        print("[ERROR] No eligible nodes found under load threshold.")
        exit(1)

    hosts_param = ",".join(nodes)

    # Step 1: Load data
    load_cmd = [
        "./bin/ycsb", "load", "cassandra-cql",
        "-P", WORKLOAD_PATH,
        "-p", f"hosts={hosts_param}",
        "-p", f"cassandra.consistencylevel={CONSISTENCY}",
        "-p", f"cassandra.table={TABLE}"
    ]
    print(f"[INFO] Loading data with consistency {CONSISTENCY} on hosts: {hosts_param}")
    subprocess.run(load_cmd, cwd=YCSB_PATH)

    # Step 2: Run workload
    run_cmd = [
        "./bin/ycsb", "run", "cassandra-cql",
        "-P", WORKLOAD_PATH,
        "-p", f"hosts={hosts_param}",
        "-p", f"cassandra.consistencylevel={CONSISTENCY}",
        "-p", f"cassandra.table={TABLE}"
    ]
    print(f"[INFO] Running workload with consistency {CONSISTENCY} on hosts: {hosts_param}")
    subprocess.run(run_cmd, cwd=YCSB_PATH)
