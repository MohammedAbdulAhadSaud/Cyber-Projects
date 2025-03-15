#!/bin/bash

# To check CPU and memory usage
check_system_usage() {
    # CPU usage
    cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')

    # Memory usage
    mem_usage=$(free | awk '/Mem/{printf("%.2f"), $3/$2*100}')

    # You can get the system usage
    echo "System Usage Report"
    echo "-------------------"
    echo "CPU Usage: $cpu_usage%"
    echo "Memory Usage: $mem_usage%"
}
