# middleware/utils.py
import subprocess
import re
from typing import List, Dict

LOAD_THRESHOLD = 50  # حداکثر طول صف پردازشی قابل قبول برای انتخاب نود

def get_active_nodes() -> List[str]:
    result = subprocess.run(["nodetool", "status"], capture_output=True, text=True)
    active_nodes = []
    for line in result.stdout.splitlines():
        if line.startswith("UN"):
            parts = line.split()
            if len(parts) >= 2:
                ip_address = parts[1]
                active_nodes.append(ip_address)
    return active_nodes

def get_node_queue_lengths(active_nodes: List[str]) -> Dict[str, int]:
    queue_lengths = {}
    for ip in active_nodes:
        try:
            result = subprocess.run(["nodetool", "-h", ip, "tpstats"], capture_output=True, text=True, timeout=5)
            for line in result.stdout.splitlines():
                if line.startswith("MutationStage"):
                    parts = line.split()
                    if len(parts) >= 5:
                        queue_length = int(parts[4])
                        queue_lengths[ip] = queue_length
        except Exception as e:
            print(f"Error retrieving tpstats from {ip}: {e}")
    return queue_lengths

def get_active_nodes_with_load() -> List[Dict]:
    active_nodes = get_active_nodes()
    queue_lengths = get_node_queue_lengths(active_nodes)
    return [{"ip": ip, "load": queue_lengths.get(ip, 0)} for ip in active_nodes]

def select_nodes_under_threshold(threshold: int = LOAD_THRESHOLD) -> List[str]:
    nodes_with_load = get_active_nodes_with_load()
    selected = [entry["ip"] for entry in nodes_with_load if entry["load"] <= threshold]
    return selected


def sort_nodes_by_load(queue_lengths: Dict[str, int]) -> List[str]:
    return sorted(queue_lengths, key=queue_lengths.get)
