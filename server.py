import threading
import time
import random

import socket

try:
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[S]: Server socket created")
except socket.error as err:
    print('socket open error: {}\n'.format(err))
    exit()

server_binding = ('', 50007)
ss.bind(server_binding)
ss.listen(1)
host = socket.gethostname()
print("[S]: Server host name is {}".format(host))
localhost_ip = (socket.gethostbyname(host))
print("[S]: Server IP address is {}".format(localhost_ip))
csockid, addr = ss.accept()

## csockid is the socket object

print ("[S]: Got a connection request from a client at {}".format(addr))

# send a intro message to the client.  
msg = "Welcome to CS 352!"
csockid.send(msg.encode('utf-8'))



# Receiving new data - Part 4
data = csockid.recv(100)

if data:
    msg = data.decode('utf-8')
    print(f"[S]Received msg:{msg}")
    msg = msg + "-added on"    
    csockid.send(msg.encode('utf-8'))

# Close the server socket
ss.close()
exit()