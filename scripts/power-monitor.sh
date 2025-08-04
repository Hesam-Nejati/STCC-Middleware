#!/bin/bash
# Monitor real-time power and CPU usage during YCSB benchmarking

mkdir -p logs
DSTAT_LOG=logs/dstat_log.csv
POWER_LOG=logs/power_logs.csv
ENERGY_SUMMARY=logs/energy_summary.txt

echo "timestamp,power_watts" > $POWER_LOG
echo "Monitoring started at: $(date)"

# Start dstat in background
dstat -cdnm --output $DSTAT_LOG 1 > /dev/null &
DSTAT_PID=$!

# Track power for 60 seconds (or customize duration)
START_TIME=$(date +%s)
for i in {1..60}; do
  # Replace line below with actual SNMP or WattsUp Pro reading
  WATTS=$(awk "BEGIN {print 30 + (RANDOM % 6)}")
  echo "$(date +%s),$WATTS" >> $POWER_LOG
  sleep 1
done
END_TIME=$(date +%s)

# Cleanup
kill $DSTAT_PID
DURATION=$((END_TIME - START_TIME))

# Energy = Avg_Power * Time
AVG_POWER=$(tail -n +2 $POWER_LOG | awk -F',' '{sum+=$2} END {print sum/NR}')
ENERGY=$(awk "BEGIN {printf \"%.3f\", $AVG_POWER * $DURATION / 3600}")

echo "Duration: $DURATION seconds" > $ENERGY_SUMMARY
echo "Average Power: $AVG_POWER W" >> $ENERGY_SUMMARY
echo "Total Energy: $ENERGY Wh" >> $ENERGY_SUMMARY

echo "Monitoring complete. Logs saved to logs/"
