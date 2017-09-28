import socket

text = raw_input("Enter text: ")

s = socket.socket()
#host = socket.gethostname()
host = '192.168.1.10'
port = 12345

print(host)
print(port)

s.connect((host, port))
s.send(str(text))
print s.recv(1024)
s.close
