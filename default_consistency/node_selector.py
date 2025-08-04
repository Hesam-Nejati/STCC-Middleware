#default_consistency/node_selector.py

import yaml
from middleware.utils import get_active_nodes_with_load

CONFIG_PATH = "middleware/config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def select_best_nodes_across_dcs():
    config = load_config()
    replication_config = config['replication']['datacenters']
    active_nodes_with_load = get_active_nodes_with_load()
    active_ips = {entry['ip']: entry['load'] for entry in active_nodes_with_load}

    selected_nodes = []

    for dc_name, dc_config in replication_config.items():
        rf = dc_config['replication_factor']
        dc_nodes = dc_config.get('nodes', [])

        dc_active = [
            {'ip': ip, 'load': active_ips[ip]}
            for ip in dc_nodes if ip in active_ips
        ]

        dc_sorted = sorted(dc_active, key=lambda x: x['load'])
        dc_selected = [n['ip'] for n in dc_sorted[:rf]]
        selected_nodes.extend(dc_selected)

    return selected_nodes

def select_target_nodes_under_threshold(threshold: int):
    """
    انتخاب نودهای فعال با بار کاری کمتر از مقدار threshold داده شده.
    خروجی: لیست IP نودهای انتخاب‌شده
    """
    active_nodes_with_load = get_active_nodes_with_load()
    selected = [node['ip'] for node in active_nodes_with_load if node['load'] <= threshold]
    return selected

# برای تست
if __name__ == "__main__":
    print("[Best Nodes by DC]:", select_best_nodes_across_dcs())
    print("[Nodes under threshold]:", select_target_nodes_under_threshold(threshold=5))
