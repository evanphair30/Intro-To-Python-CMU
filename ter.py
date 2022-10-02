
import datetime
import socket
import sys
import os
import urllib3
import requests
from datetime import datetime

#program = sys.argv[0]
hostname = sys.argv[1]
arg2 = sys.argv[2]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = requests.get(hostname, verify=False, timeout=int(arg2)).elapsed.total_seconds() # 10 seconds

if r < 1:
 print ("Low response time")
else:
 print ("High response time")

print (hostname)


print (current_time,hostname,r)


line = "{}\t{}\t{}\n".format(current_time, hostname, r)
 
with open("foo.log", "a") as f:
    f.write(line)