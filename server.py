#!/usr/bin/python

import os, socket

s = socket.socket()
host = socket.gethostname()
port = 12345

print(host)
print(port)

s.bind(('', port))

s.listen(5)
while True:
   c, addr = s.accept()
   print 'Got connection from', addr
   #print c.recv(1024)
   stream = c.recv(1024)
   command = stream.decode('utf-8')
   print("Command is " + str(command))	
   os.system(command)
   c.send('Received... transmitting files for x')
   c.close()
