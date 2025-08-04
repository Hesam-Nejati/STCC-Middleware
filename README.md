# STCC-Enabled Cassandra Benchmark Suite

This repository provides a structured environment for evaluating and comparing the **Strict Timed Causal Consistency (STCC)** model against Cassandra's default consistency levels (`ALL`, `QUORUM`, `ONE`). It includes STCC middleware logic, custom YCSB integration, and default consistency runners to benchmark performance, consistency, and scalability.

---

## 📁 Directory Structure

```
├── cassandra.service              # Optional systemd unit for Cassandra node startup
├── install_cassndra.md            # Setup guide to install and configure Apache Cassandra
├── Cassandra_README.md            # Extended technical documentation for architecture and usage
├── README.md                      # You are here
├── logs/
│   └── ops_log.db                # SQLite DB tracking operations for STCC dependency analysis
├── middleware/                    # Core STCC middleware logic and operation routing
│   ├── main.py                   # FastAPI app exposing /api/execute
│   ├── routing.py                # REST router (POST /api/execute)
│   ├── consistency.py            # STCC logic for enforcing MR, MW, RYW, WFR, UGD
│   ├── cassandra_client.py       # Dispatches validated ops to selected Cassandra nodes
│   ├── odg.py                    # Tracks and enforces user-generated dependencies (UGD)
│   ├── node_selector.py          # Picks low-load nodes under threshold for distribution
│   ├── utils.py                  # System-level monitoring using nodetool (UN, tpstats)
│   ├── config.yaml               # Config for datacenters, STCC thresholds, features
│   └── run_stcc_ycsb.py          # CLI runner: loads + runs YCSB workloads line-by-line via middleware
├── default_consistency/          # Baseline runners using Cassandra's built-in consistency
│   ├── default_all.py            # Runs YCSB workloads with ConsistencyLevel.ALL
│   ├── default_one.py            # Runs with ConsistencyLevel.ONE
│   ├── default_quorum.py         # Runs with ConsistencyLevel.QUORUM
│   ├── config.yaml               # Cluster node list for baseline consistency runners
│   ├── node_selector.py          # Node load checker for fair workload distribution
│   ├── utils.py                  # Load-aware node selection logic
│   ├── main.py                   # (Optional) API server entrypoint (not used)
│   └── routing.py                # (Unused) Placeholder for default runner routing
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
- Python 3.8+
- FastAPI, requests, sqlite3

---

## 🧠 Citation
If you use this implementation in your research or industrial projects, please cite our corresponding paper (under submission).

---

For questions, contact the author via GitHub or email.


Email: hesam.nejati@gmail.com
