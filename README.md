# STCC-Enabled Cassandra Benchmark Suite

This repository provides a structured environment for evaluating and comparing the **Strict Timed Causal Consistency (STCC)** model against Cassandra's default consistency levels (`ALL`, `QUORUM`, `ONE`). It includes STCC middleware logic, custom YCSB integration, and default consistency runners to benchmark performance, consistency, energy, and scalability.

---

## 📁 Directory Structure

```
├── Cassandra_README.md
├── cassandra.service
├── CITATION.cff
├── data_analysis
│   ├── case_study_workload_a.py
│   ├── case_study_workload_b.py
│   ├── case_study_workload_c.py
│   ├── dynamic_power_wa_full_1.py
│   ├── dynamic_power_wa_partial.py
│   ├── dynamic_power_wb_full_1.py
│   ├── dynamic_power_wb_partial.py
│   ├── dynamic_power_wc_full_1.py
│   ├── dynamic_power_wc_partial.py
│   ├── energy_execution_full_wa_one.py
│   ├── energy_execution_full_wa.py
│   ├── energy_execution_full_wa_quorum.py
│   ├── energy_execution_full_wb_one.py
│   ├── energy_execution_full_wb.py
│   ├── energy_execution_full_wb_quorum.py
│   ├── energy_execution_full_wc_one.py
│   ├── energy_execution_full_wc.py
│   ├── energy_execution_full_wc_quorum.py
│   ├── network_latancy-full-wa.py
│   ├── network_latancy-full-wb.py
│   ├── network_latancy-full-wc.py
│   ├── network_latancy-partial-wa.py
│   ├── network_latancy-partial-wb.py
│   ├── network_latency-partial-wc.py
│   ├── network_latency_vs_no_nodes.py
│   ├── netwrok_latency_replication_factor.py
│   ├── power_predict_new.py
│   ├── power_predict.py
│   ├── power_vs_node.py
│   ├── throughput_vs_number_of_nodes.py
│   ├── throughput_vs_replication_factor.py
│   ├── throughput-wa.py
│   ├── throughput-wb.py
│   └── throughput-wc.py
├── default_consistency
│   ├── config.yaml
│   ├── default_all.py
│   ├── default_one.py
│   ├── default_quorum.py
│   ├── __init__.py
│   ├── main.py
│   ├── node_selector.py
│   ├── routing.py
│   └── utils.py
├── figure
│   ├── cassandra-monitoring-1-opscenter.jpg
│   ├── cassandra_yaml_change_cluster_nme
│   ├── cqlsh.png
│   ├── create_keyspace.png
│   ├── create_ycsb_table.png
│   ├── middleware.pdf
│   ├── network_topology_strategy.webp
│   ├── nodetool_cfstats_user_network_topology_ycsb.png
│   ├── nodetool_status.png
│   ├── nodetool_tpstats.png
│   ├── odg.png
│   ├── opscenter_1043873.jpg
│   ├── output.png
│   ├── read_write_latency.png
│   ├── sample_ycsb_result_in_terminal_linux.png
│   ├── workload_a.png
│   ├── workload_b.png
│   └── workload_c.png
├── install_cassndra.md
├── LICENSE
├── logs
│   ├── ops_log.db
│   ├── structured_ycsb_data.csv
│   ├── structured_ycsb_data.json
│   ├── ycsb_energy_data_runtime.csv
│   └── ycsb_energy_data_runtime.json
├── middleware
│   ├── cassandra_client.py
│   ├── config.yaml
│   ├── consistency.py
│   ├── __init__.py
│   ├── main.py
│   ├── node_selector.py
│   ├── odg.py
│   ├── routing.py
│   ├── run_stcc_ycsb.py
│   └── utils.py
├── README.md
├── scripts
│   └── power-monitor.sh
└── YCSB_README.md
```

---

## 🚀 Usage Overview

### 🔧 Step 1: Set Up Cassandra Cluster
- Deploy Apache Cassandra across your desired nodes
- Configure **NetworkTopologyStrategy** replication using `config.yaml`
- Ensure `nodetool status` and `tpstats` return valid responses on all nodes

### 🧠 Step 2: Run STCC-enabled YCSB Workload
```bash
python middleware/run_stcc_ycsb.py
```
- Select workload `a`, `b`, or `c` when prompted
- Automatically loads dataset to low-load nodes
- Each operation is parsed and sent to the STCC API:
  - Enforces **Monotonic Read**, **Monotonic Write**, **Read Your Writes**, **Write-Follow-Read**, and **User-Generated Dependencies**
  - Sends validated requests to optimal Cassandra nodes for execution

### 📊 Step 3: Run Baseline Cassandra Consistency for Comparison
```bash
python default_consistency/default_all.py      # For ConsistencyLevel.ALL
python default_consistency/default_quorum.py   # For ConsistencyLevel.QUORUM
python default_consistency/default_one.py      # For ConsistencyLevel.ONE
```
- Each script:
  - Picks low-load nodes
  - Loads and runs YCSB directly with chosen consistency level
  - No STCC logic is applied (baseline)

---

## 🔍 Key Concepts
- **STCC** = Client-enforced consistency logic using operation logs and timestamp verification
- **YCSB Integration** = Instead of sending workload to Cassandra directly, YCSB operations are parsed and sent line-by-line to the middleware
- **UGD Detection** = STCC middleware uses `ops_log.db` to enforce cross-user consistency semantics

---

## ⚡ Step 4: Real-Time Power and CPU Monitoring:
To evaluate the energy efficiency and system overhead of each consistency model, we provide an optional ...

🔍 What It Measures:
CPU Usage (%) per second via dstat

Power Draw (Watts) from PDU or WattsUp Pro via SNMP or log extraction

Total Energy Consumption (Wh or Joules) after each run

🛠️ How It Works:
The script scripts/power-monitor.sh launches:

A background process using dstat to log CPU statistics

A loop (or SNMP poll) to collect power values every second

Synchronization with benchmark start/end times

---

## 🧪 Workloads
Place your workload files in:
```
YCSB/workloads/workloada
YCSB/workloads/workloadb
YCSB/workloads/workloadc
```
Each workload must follow YCSB command format:
```
INSERT user42 ykey123 field0=val0 field1=val1
READ user42 ykey123
UPDATE user42 ykey123 field1=newval
DELETE user42 ykey123
```

---

## 📦 Dependencies
- Apache Cassandra (≥ v4.x)
- Python 3.12.3
- FastAPI, requests, sqlite3

---

For questions, contact the author via GitHub or email.


Email: hesam.nejati@gmail.com

## 📜 License and Citation

This project is released under the [MIT License](./LICENSE).

🔒 **Usage of this software requires citation** of the following publication:

> H. Nejati Sharif, H. Deldari, M.H. Moattar, M.R. Ghods,  
> *Strict timed causal consistency as a hybrid consistency model in the cloud environment*,  
> Future Generation Computer Systems, Vol. 105, 2020, pp. 259–274.  
> [https://doi.org/10.1016/j.future.2019.12.018](https://doi.org/10.1016/j.future.2019.12.018)

> H. Nejati Sharifaldin, F. Nayebi Pour,
> *An Industrial Benchmarking Suite for Energy–Performance–Consistency Trade-Offs in Apache Cassandra with Middleware-Enforced Timed Causal Consistency and Static Consistency Levels*,
> [https://github.com/Hesam-Nejati/STCC-Middleware] Aug, 2025.
> [https://doi.org/10.5281/zenodo.16742599](https://doi.org/10.5281/zenodo.16742599)
 

