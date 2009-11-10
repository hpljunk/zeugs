# Demonstrates various methods of importing modules.
from socket import *
import string
import time
import sys

# create a socket of the basic type.
s = socket(AF_INET, SOCK_STREAM)
# define our banner.
senddata1 = "220 desktop Microsoft ESMTP MAIL Service, Version 6.0.2600.1106 ready at" + time.strftime("%a, %d %b %Y %H:%M:%S %Z")
# Query the user for their IP Address and set that and the port
HOST = '192.168.123.69' # raw_input("Enter IP Address to bind socket to: ")
PORT = 2000
s.bind((HOST, PORT)) # Bind the socket to an IP Address and Port
s.listen(1) # Have the socket listen for a connection
(incomingsocket, address) = s.accept() # Accept an incoming connection
incomingsocket.send(senddata1) # Send our banner
straddress = str(address) # Convert incoming address to a string
testlist = string.split(straddress, ",") # Split the tuple into lists
gethost = string.split(testlist[0], "'") # Split the host portion of the list
getaddr = string.split(testlist[1], ")") # Split the port portion of the list
host = gethost[1] # Remove just the address from the list
incomingport = int(getaddr[0]) # Remove just the port from the list
# define our Warning
senddata2 = "Illegal Access of this server, your IP [" + host +"] has been logged." 
# Print connection information to the stdout
print "Connection attempt on port", PORT, "from", host, ":", incomingport
# Listen for incoming data
data = incomingsocket.recv(1024)
string =""
timeakt =time
# Send the Warning
#incomingsocket.send(senddata2)
while len(data):
  string = string + data
  data = incomingsocket.recv(1024)
  #print "data flow \r ["+ string +"] log"
  print "data from",host,"  @",timeakt," \r"
  if not data: break 

incomingsocket.close()
print string
sys.exit(0)

#links
#http://code.activestate.com/recipes/408859/
#http://www.python-forum.de/viewtopic.php?p=140232&sid=36ee17cc423cc02592d5b3f53d6ceb54
#next link tuppel to int!
#http://stackoverflow.com/questions/691345/handling-output-of-python-socket-recv