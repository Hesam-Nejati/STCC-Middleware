# STCC-Enabled Cassandra Benchmark Suite

This repository provides a structured environment for evaluating and comparing the **Strict Timed Causal Consistency (STCC)** model against Cassandra's default consistency levels (`ALL`, `QUORUM`, `ONE`). It includes STCC middleware logic, custom YCSB integration, and default consistency runners to benchmark performance, consistency, energy, and scalability.

---

## 📁 Directory Structure

```
├── Cassandra_README.md
├── cassandra.service
├── CITATION.cff
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
├── install_cassndra.md
├── LICENSE
├── logs
│   ├── dstat_log.csv
│   ├── energy_summary.txt
│   ├── ops_log.db
│   └── power_logs.csv
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

## Step 4:  Real-Time Power and CPU Monitoring:
To evaluate the energy efficiency and system overhead of each consistency model, we provide an optional s>

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
