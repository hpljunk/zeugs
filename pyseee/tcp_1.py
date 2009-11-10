# -*- coding: utf-8 -*-
#! python
#!/usr/bin/env python
import socket
import sys

HOST = '192.168.123.33'
GET = '/rss.xml'
PORT = 2000
conhost = ''
try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  sys.stderr.write("[ERRORxxx] %s\n" % msg[1])
  sys.exit(1)

try:
  sock.accept(conhost)
except socket.error, msg:
    sys.stderr.write("[ERRORyyyy] %s\n" % msg[1])
    sys.exit(2)

#sock.send("GET %s HTTP/1.0\r\nHost: %s\r\n\r\n" % (GET, HOST))
data = sock.recv(1024)
string = ""

while len(data):
  string = string + data
  data = sock.recv(1024)

sock.close()
print string
sys.exit(0)