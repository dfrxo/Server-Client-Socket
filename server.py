import threading
import time
import random

import socket

def swap(word):
    txt = word[::-1]
    new_string = ""
    for c in txt:
        if ord(c) < 91 and ord(c) > 64:
            c = ord(c) + 32
            new_string+=chr(c)

        elif ord(c) > 96 and ord(c) < 123:
            c = ord(c) - 32
            new_string+=chr(c)
        else:
            new_string+=(c)
    #print(new_string)
    return new_string

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
data = csockid.recv(102400)  # Combined list of lines seperated by \n # Parameter means number of bytes
data = data.decode('utf-8')
data = data.split('\n')   # Split into list of lines
if len(data[len(data)-1]) == 0:
    data.pop()                # Pop last element - extra \n character
csockid.send("Nice".encode('utf-8')) # Nice

with open("out-proj.txt", "w") as wtr: # (file, mode)
    for i, line in enumerate(data):
        new_line = swap(line) + "\n"
        wtr.write(new_line) # Write to file
        
csockid.close()
# Close the server socket
ss.close()
exit()