import socket
import sys
from numpy import *
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)



d,t,f=genfromtxt("parout.csv",delimiter='\t',unpack='True')

db=[struct.pack('f',d[i]) for i in range(10000)]



#bytelist=db[0]
for i in range(2):
    for j in range(10):
        bytelist=bytelist+db[j+i*100]
    sent = sock.sendto(bytelist, server_address)



# Send data
#for i in range(len(db)):
#    sock.sendto(db[i], server_address)
#    print("sent message:",i)


