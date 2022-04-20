# dc_tracks_loader

Checkout the project

Make sure the creds are correct for confluent in each of the .py files

Run the ingester run_ingestor.sh

The ingestor will run indefinitely, so to kill it you need to control-c and then run:
kill `ps -ef | grep cload | awk {'print $2'}`

