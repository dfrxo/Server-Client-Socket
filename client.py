import threading
import time
import random

import socket

try:
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[C]: Client socket created")
except socket.error as err:
    print('socket open error: {} \n'.format(err))
    exit()
    
# Define the port on which you want to connect to the server
port = 50007
localhost_addr = socket.gethostbyname(socket.gethostname())

# connect to the server on local machine
server_binding = (localhost_addr, port)
cs.connect(server_binding)

# Receive data from the server
data_from_server=cs.recv(100)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))




# Sending new data
# Read data from file
file = open(r"in-proj.txt", "r")
#content = str(file.readlines())   # Put data into a list of strings (each index is a line) and convert to string

content = file.readlines()   # Put data into a list of strings (each index is a line) and convert to string
msg = ""
#print(content)
for line in content:
    msg = msg + line
    
print(msg)
#msg = msg.split("\n")


cs.send(msg.encode('utf-8'))
data_from_server=cs.recv(100)
print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

# close the client socket
cs.close()
exit()