✅ Step-by-Step: Creating a Manual systemd Service for Cassandra
✳️ Step 1: Create the systemd service file
# Run the following command to create the service file:

- sudo nano /etc/systemd/system/cassandra.service

# Paste the following content into the file (adjust paths and user accordingly):

[Unit]
Description=Apache Cassandra
After=network.target

[Service]
Type=simple
User=hesam
Group=hesam
[Service]
Environment="JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64"
Environment="CASSANDRA_CONF=/home/hesam/Desktop/web-project/cassandra/apache-cassandra-4.1.8/conf"
WorkingDirectory=/home/hesam/Desktop/web-project/cassandra/apache-cassandra-4.1.8
ExecStart=/home/hesam/Desktop/web-project/cassandra/apache-cassandra-4.1.8/bin/cassandra -f -R
ExecStop=/bin/kill -15 $MAINPID
Restart=on-failure
RestartSec=5
LimitNOFILE=100000
TimeoutStopSec=30

[Install]
WantedBy=multi-user.target

# Write your own directory

ExecStart=/home/hesam/Desktop/web-project/backend/apache-cassandra/bin/cassandra -f

⚠️ Note: If Java is not found...
# Cassandra may require JAVA_HOME to be set explicitly.
# If you see an error related to Java in the logs, make sure the following line is added before ExecStart:

Environment="JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64"

✅ How to Install Java with apt (and change versions)
Step-by-step instructions:

1. Install OpenJDK (e.g., **Java 8** or **Java 11**):

- sudo apt update

**Java 8**
- sudo apt install openjdk-8-jdk

**Java 11**:

- sudo apt install openjdk-11-jdk

2. Check installed Java versions:

- update-java-alternatives --list

3. Switch between Java versions:

- sudo update-alternatives --config java

Select the version you want by typing the corresponding number.

4. Check the currently active Java version:

- java -version

✅ Change Ownership of Cassandra Directory to Your User

# To ensure you have permission to run everything, transfer ownership to your user:

- sudo chown -R $USER:$USER /path/to/destination/apache-cassandra-4.1.8

# This gives full access to all Cassandra files and directories under your username.

✅ Make Cassandra Executable
# Ensure the Cassandra binary is executable:

- chmod +x /path/to/destination/apache-cassandra-4.1.8/bin/cassandra

✅ Start and Manage the Cassandra Service:

# Warning: The unit file, source configuration file or drop-ins of cassandra.service changed on disk. Run 'systemctl daemon-reload' to reload units.

- systemctl daemon-reload

# Start the service:

- sudo systemctl start cassandra

# Restart the service:

- sudo systemctl restart cassandra

# Check the service status:

- sudo systemctl status cassandra

# Stop the service:

- sudo systemctl stop cassandra


🧪 If Something Goes Wrong: Check Logs
# To see the latest logs:

- journalctl -u cassandra -n 50 --no-pager

✅ Cassandra Python Driver and CLI Tools
# Install the Python Cassandra driver:

- pip install cassandra-driver
- pip install six

# Install cqlsh via Snap:

- sudo snap install cqlsh


