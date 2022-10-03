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
import time
import urllib3
import requests
from urllib.parse import urlparse
from datetime import datetime

#program = sys.argv[0]
hostname = sys.argv[1]
arg2 = sys.argv[2]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = requests.get(hostname, verify=False, timeout=int(arg2)).elapsed.total_seconds() # 10 seconds


print (hostname)

#print ("Start : %s" % time.ctime())
#time.sleep(int(arg2))
#print ("End : %s" % time.ctime())

#class test:
#    if not r:
#        print (current_time,hostname,'DOWN',r)
#    else:
#        print (current_time,hostname,'UP',r)


#print (current_time,hostname,r)

parsed = urlparse(hostname)
hostnames = parsed.hostname
ipaddress = socket.gethostbyname(hostnames)

print (ipaddress)
#IPAddr=socket.gethostbyname(urlparse(hostname))

#while True:
#    os.system('cls')

#    if ipaddress == 'quit':
#        print('script terminated')
#        break
#    else:
#        os.system('ping -n ' + ipaddress)

#yes = time.sleep(int(arg2))

count = 0
while (count < int(arg2)):
    if not r:
        d=('DOWN')
        print (current_time,hostname,d,r)
    else:
        u=('UP')
        print (current_time,hostname,u,r)
    count = count + 1



line = "{}\t{}\t{}\n".format(current_time, hostname, r)
 
with open("foo.log", "a") as f:
    f.write(line)
