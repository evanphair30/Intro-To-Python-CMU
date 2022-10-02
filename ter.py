#[10 points] Write a program that sends an HTTP GET request to a website every X (configurable)
#seconds and determines whether the site is up or not based on its response (or lack thereof). Store the
#results in a tab-delimited file named uptime.txt, appending each new result. Record the response time in
#milliseconds for each request. Your program should keep running until the user forces it to close using
#CTRL+C (or the equivalent on your operating system).
#The CLI interface should look like:
#monitor.py <url> <seconds>
#A typical user interaction might look like:
#$ python monitor.py https://www.cmu.edu 30
#<user lets the program run for a few minutes, and then hits CTRL+C>

#Once the program has completed, the contents of uptime.txt might be:
# 01:30:35 https://www.cmu.edu UP 100
# 01:31:05 https://www.cmu.edu UP 89
# 01:31:35 https://www.cmu.edu UP 88
# 01:32:05 https://www.cmu.edu DOWN *
# 01:32:35 https://www.cmu.edu UP 106
# 01:33:05 https://www.cmu.edu UP 95
# ...
#This result file indicates that https://www.cmu.e du was down for at most 59 seconds between 01:31:36
#and 01:32:35. The last value of each line is the response time (ms). Note that its a * for the failed
#request, since there was no response time.
#What to submit:
#You should upload a single file named monitor.py

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


print (hostname)

if not r:
    print ('DOWN')
else:
    print ('UP')

print (current_time,hostname,r)


line = "{}\t{}\t{}\n".format(current_time, hostname, r)
 
with open("foo.log", "a") as f:
    f.write(line)
