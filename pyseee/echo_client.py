# Echo client program
import socket

HOST = '192.168.123.33'                 # Symbolic name meaning all available interfaces
PORT = 2042          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
