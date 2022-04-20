import sys
import gpudb
import csv
from datetime import datetime
import _thread
import time
import random
import decimal
from kafka import KafkaProducer
import logging
import json


thefile=sys.argv[1]
streaming_data = csv.reader(open(thefile))
next(streaming_data)
got_recs = []
counter = 0
producer = KafkaProducer(bootstrap_servers=["pkc-ep9mm.us-east-2.aws.confluent.cloud:9092"],
sasl_plain_username = "3QZHOEVCAHHFUZWH",
sasl_plain_password = "O+n9UEvSkj0s2Kv6PDBTuAtJmO2RcbxNTTl23+D4vsGVkZ09yYFewakwTLpuuh1p",
security_protocol="SASL_SSL",
sasl_mechanism="PLAIN",
value_serializer=lambda x:
json.dumps(x).encode('utf-8'))
print('Connecting to Kafka, completed')
for record in streaming_data:
   now = datetime.now()
   timestamp = datetime.timestamp(now)

   now = datetime.now()
   timestamp = datetime.timestamp(now)
 
   payload = {
   "ID" : record[0],
   "cycle" : record[1],
   "setting1" : record[2],
   "setting2" : record[3],
   "setting3" : record[4],
   "concentration" : record[5],
   "flow_rate" : record[6],
   "compression" : record[7],
   "pressure" : record[8],
   "volume" : record[9],
   "mats" : record[10],
   "dense" : record[11],
   "volt" : record[12],
   "cap" : record[13],
   "stdev" : record[14],
   "temp" : record[15],
   "s12" : record[16],
   "s13" : record[17],
   "s14" : record[18],
   "s15" : record[19],
   "s16" : record[20],
   "s17" : record[21],
   "s18" : record[22],
   "s19" : record[23],
   "s20" : record[24],
   "s21" : record[25],
   "ttf" : record[26],
   "ts" : int(timestamp*1000)
   }

   print(payload)
   producer.send('vehicle_metrics', value=payload)
   time.sleep(0.5)
   producer.flush()
