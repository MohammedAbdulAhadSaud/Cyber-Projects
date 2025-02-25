#!/bin/bash

INTERFACE="eth0"  # Change this to your network interface

while true; do
    # Change the MAC address
    sudo macchanger -r $INTERFACE
    echo "MAC address changed for $INTERFACE"
    
    # Wait for 3 minutes (180 seconds)
    sleep 180
done
      
