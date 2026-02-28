#!/bin/bash
while true; do
	read USED AVAILABLE < <(free -h| awk '/^Mem:/ {print $3, $7}')
	echo "$(date +%T) | RAM usada: $USED | Avail: $AVAILABLE" >> /tmp/used_ram.log
	
	sleep 15
done
