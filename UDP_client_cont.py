import socket
import sys
from numpy import *
import struct
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

chunck=10000

d,t,f=genfromtxt("parout.csv",delimiter='\t',unpack='True')


#d=[i for i in range(chunck)]
db=[struct.pack('f',d[i]) for i in range(chunck)]


framelen=20

for i in range(int(chunck/framelen)):
    bytelist=db[i*framelen]
    for j in range(1,framelen):
        bytelist=bytelist+db[j+i*framelen]
    print("data n: ",i)
    print(struct.unpack('f',db[(framelen-1)+i*framelen]))
    #time.sleep(0.05)
    sent = sock.sendto(bytelist, server_address)



# Send data
#for i in range(len(db)):
#    sock.sendto(db[i], server_address)
#    print("sent message:",i)


