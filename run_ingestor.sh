#!/bin/bash

while [[ true ]]
	do
	for f in {1..10}
	do
		python3 ./locations_cload.py ${f}.csv >/dev/null  & 
		python3 ./metrics_cload.py ${f}_metrics.csv >/dev/null & 
	done
	wait
done
