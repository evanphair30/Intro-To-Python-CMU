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
import requests as req

#program = sys.argv[0]
hostname = sys.argv[1]
#arg2 = sys.argv[2]

#resp = req.get(hostname)

# ts stores the time in seconds
ts = datetime.datetime.now()
  
#try:
#    time = req.get(hostname).elapsed.total_seconds(arg2)
#    if time < 1:
#        print ("Low response time")
#    else:
#        print ("High response time")
#except:
#    # threw an exception
#    print ("High response time")

response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print (ts, hostname, 'UP')
else:
  print (ts, hostname, 'DOWN')

print (hostname)
