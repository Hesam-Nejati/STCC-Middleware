# 📦 Apache Cassandra Installation & Configuration Guide (Manual)

This document provides step-by-step instructions to manually install, configure, and run Apache Cassandra locally for development purposes.

---

## 🔽 1. Download Apache Cassandra

Download the desired version from the official Apache Cassandra website:

👉 [Download Cassandra 4.1.8](https://downloads.apache.org/cassandra/4.1.8/apache-cassandra-4.1.8-bin.tar.gz)

---

## 📂 2. Extract and Setup Directory

```bash
tar -xzvf apache-cassandra-4.1.8-bin.tar.gz

# (Optional) Create a symbolic link for easier access:

- ln -s apache-cassandra-4.1.8/ /your/path/cassandra

📁 3. Create Required Data and Log Directories

# Navigate into the Cassandra directory:

- cd /your/path/cassandra/

mkdir -p data/data
mkdir -p data/saved_caches
mkdir -p data/commitlog
mkdir logs

# These directories are used by Cassandra to store persistent data, logs, and cache files.

⚙️ 4. Edit Configuration Files
# Navigate to the config directory:

- cd /your/path/cassandra/

- cd conf

**cassandra.yaml**

# Edit the main configuration file:

- nano cassandra.yaml

# Modify the following fields:

cluster_name: 'My Cluster'
num_tokens: 256
max_hint_window_in_ms: 3600000  # Enables hinted handoff for 1 hour

# Development-mode authenticator/authorizer (disable for production)
authenticator: AllowAllAuthenticator
authorizer: AllowAllAuthorizer
role_manager: CassandraRoleManager
network_authorizer: AllowAllNetworkAuthorizer

# Cluster communication
seed_provider:
  - class_name: org.apache.cassandra.locator.SimpleSeedProvider
    parameters:
      - seeds: "192.168.0.137"

listen_address: 192.168.0.137
rpc_address: 192.168.0.137

# Snitch for topology awareness
endpoint_snitch: GossipingPropertyFileSnitch

cassandra-topology.properties.example
# Defines the IP-to-datacenter/rack mappings:

- nano cassandra-topology.properties.example

# Example content:

# Cassandra Node IP = DataCenter:Rack
192.168.0.137=DC1:RAC1
192.168.1.100=DC1:RAC1
192.168.2.200=DC2:RAC2

10.0.0.10=DC1:RAC1
10.0.0.11=DC1:RAC1
10.0.0.12=DC1:RAC2

10.20.114.10=DC2:RAC1
10.20.114.11=DC2:RAC1

10.21.119.13=DC3:RAC1
10.21.119.10=DC3:RAC1

10.0.0.13=DC1:RAC2
10.21.119.14=DC3:RAC2
10.20.114.15=DC2:RAC2

default=DC1:r1

cassandra-rackdc.properties
# Specify the DC and Rack of this node:

- nano cassandra-rackdc.properties

dc=DC1
rack=RAC1






