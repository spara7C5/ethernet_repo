import socket
import sys
from numpy import *
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)



d,t,f=genfromtxt("parout.csv",delimiter='\t',unpack='True')

db=[struct.pack('f',d[i]) for i in range(len(d))]


# Send data
#sent = sock.sendto(message, server_address)
sent = sock.sendto(db[0], server_address)
print("message sent")


