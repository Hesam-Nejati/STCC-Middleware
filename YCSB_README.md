# YCSB Cassandra Benchmark – Setup and Load Guide

This guide describes the necessary steps to configure, build, and load data into Apache Cassandra 4.1.8 using the Yahoo! Cloud Serving Benchmark (YCSB). The instructions are tested on Ubuntu Linux with Cassandra 4.1.8 and Java 11.

---

## 📦 Prerequisites

Ensure the following components are installed:

| Component         | Version               | Installation Notes                         |
|------------------|------------------------|---------------------------------------------|
| Java             | OpenJDK 11 or 17       | `sudo apt install openjdk-11-jdk`          |
| Apache Maven     | ≥ 3.6                  | `sudo apt install maven`                   |
| Python           | Python 3 (linked to `python`) | `sudo ln -s /usr/bin/python3 /usr/bin/python` |
| Git              | Latest stable          | `sudo apt install git`                     |
| Apache Cassandra | 4.1.8                  | Ensure it is running on port 9042          |

---

## 🔧 Step-by-Step Instructions

### 1. Clone the YCSB Repository

```bash
git clone https://github.com/brianfrankcooper/YCSB.git
cd YCSB

Build YCSB for Cassandra CQL Binding:

mvn -pl site.ycsb:cassandra-binding -am clean package


Load Initial Data into Cassandra:

./bin/ycsb load cassandra-cql -s \
  -P workloads/workloada \
  -p hosts=192.168.1.100 \ #One of the IP Address of Cassandra Nodes you use it to deploy YCSB 
  -p cassandra.keyspace=ycsb

ًRun the YCSB Data into Cassandra (example):
./bin/ycsb run cassandra-cql -s \
  -P workloads/workloada \
  -p hosts=192.168.1.100 \
  -p cassandra.keyspace=ycsb \
  -p operationcount=5000 \
  -threads 4


