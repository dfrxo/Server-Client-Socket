import os
#print(os.getcwd())


file = open(r"/common/home/df652/Documents/Server-Client-Socket/in-proj.txt", "r")
content = file.readlines()   # Put data into a list of strings (each index is a line) and convert to string

msg = ""
for line in content:
    msg+=line
msg = msg.split("\n")

