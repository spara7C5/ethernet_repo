import socket
import sys
from numpy import *
import struct
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)

chunck=12000

d,t,f=genfromtxt("parout.csv",delimiter='\t',unpack='True')


#d=[i for i in range(chunck)]
db=[struct.pack('f',d[i]) for i in range(chunck)]
tb=[struct.pack('f',t[i]) for i in range(chunck)]
fb=[struct.pack('f',f[i]) for i in range(chunck)]

frame3=600
framelen=int(frame3/3)

w=0
while 1:
    
    for i in range(int(chunck/(framelen))):
        timestart=time.time()
        bytelist=db[i*framelen]+tb[i*framelen]+fb[i*framelen]
        for j in range(1,int(framelen)):
            bytelist=bytelist+db[j+i*framelen]+tb[j+i*framelen]+fb[j+i*framelen]
        print("data n:",i+w*int(chunck/(framelen)),"time:",time.time()-timestart)
        #print(struct.unpack('f',db[(framelen-1)+i*framelen]))
        time.sleep(0.04)
        sock.sendto(bytelist, server_address)
    w+=1




