# run_stcc_ycsb.py
import subprocess
import sys
import os
import requests

from middleware.utils import get_active_nodes_with_load

# === Configuration ===
YCSB_DIR = "YCSB"
WORKLOAD_OPTIONS = {
    "a": "workloada",
    "b": "workloadb",
    "c": "workloadc"
}
API_ENDPOINT = "http://localhost:8000/api/execute"
TABLE = "user_network_topology.ycsb"
LOAD_THRESHOLD = 20

# === Prompt for workload selection ===
def choose_workload():
    print("Select workload: a, b, or c")
    choice = input("Enter choice [a|b|c]: ").strip().lower()
    if choice not in WORKLOAD_OPTIONS:
        print("Invalid choice. Use 'a', 'b', or 'c'.")
        sys.exit(1)
    return os.path.join(YCSB_DIR, "workloads", WORKLOAD_OPTIONS[choice])

# === Load data via YCSB to eligible nodes ===
def load_data(workload_path, threshold=LOAD_THRESHOLD):
    print("[INFO] Selecting eligible nodes for loading...")

    nodes_with_load = get_active_nodes_with_load()
    eligible_nodes = [entry["ip"] for entry in nodes_with_load if entry["load"] <= threshold]

    if not eligible_nodes:
        print("[ERROR] No nodes under threshold found for loading.")
        sys.exit(1)

    hosts = ",".join(eligible_nodes)
    print(f"[INFO] Loading workload via YCSB to nodes: {hosts}")

    load_cmd = [
        "./bin/ycsb", "load", "cassandra-cql",
        "-P", workload_path,
        "-p", f"hosts={hosts}",
        "-p", f"cassandra.table={TABLE}"
    ]

    subprocess.run(load_cmd, cwd=YCSB_DIR)

# === Parse a single YCSB line to operation dict ===
def parse_ycsb_line(line: str) -> dict:
    tokens = line.strip().split()
    if not tokens:
        return {}

    op_type = tokens[0].upper()
    user_id = tokens[1] if len(tokens) > 1 else "anonymous"
    y_id = tokens[2] if len(tokens) > 2 else ""
    fields = {}
    for token in tokens[3:]:
        if '=' in token:
            key, val = token.split('=', 1)
            fields[key] = val

    return {
        "operation": op_type,
        "user_id": user_id,
        "y_id": y_id,
        **fields
    }

# === Run each YCSB operation through the STCC middleware ===
def run_workload(workload_file: str):
    with open(workload_file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        op = parse_ycsb_line(line)
        if not op:
            continue

        try:
            response = requests.post(API_ENDPOINT, json=op)
            print(f"[RESPONSE] {response.status_code}: {response.json()}")
        except Exception as e:
            print(f"[ERROR] Failed to execute operation: {e}")

if __name__ == "__main__":
    workload_path = choose_workload()
    print(f"[INFO] Executing workload from: {workload_path}")

    # Step 1: Load data to distributed Cassandra nodes
    load_data(workload_path)

    # Step 2: Run line-by-line through STCC middleware
    run_workload(workload_path)
