import socket

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
   print c.recv(1024)
   c.send('Received... transmitting files for x')
   c.close()
