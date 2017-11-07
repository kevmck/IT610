#!/usr/bin/python

import os,sys

os.system("ps -e -o pid,comm,etime | grep -m 1 \"\<smbd\>\" > /tmp/temp")

fileIn = open("/tmp/temp", "r")

for line in fileIn:
    x = line
    x = x[11:]
    x = x.strip()
    stamp = x

minutes = int(x[-5:-3])
#print(x)
#print(minutes)
if len(x) > 5:
    print "OK - smbd up for " + stamp

else:
    if minutes > 15:
        print "OK - smbd up for " + stamp
        sys.exit(0)

    elif minutes > 10:
        print "WARNING - smbd up for " + stamp
        sys.exit(1)

    elif minutes > 5:
        print "CRITICAL - smbd up for " + stamp
        sys.exit(2)

    else:
        print "UNKNOWN - check service"
        sys.exit(3)
