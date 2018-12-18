
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import time

from socket import *
from struct import unpack


host = "localhost"
port = 10000
addr = (host,port)

UDPSock = socket(AF_INET,SOCK_DGRAM)
UDPSock.bind(addr)
print("socket initialized")

d,t,f=np.genfromtxt("parout.csv",delimiter='\t',unpack='True')

d=d[0:10000]
t=t[0:10000]

winlen=100
shilen=1
shitime=0.01 # equal to update time
unpstr='{}f'.format(shilen)
bytelen=4*shilen
x=range(winlen)
yd=d[0 :winlen]
yt=t[0:winlen]
dwin=yd


# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, yd)
line2,=ax.plot(x,yt)
# Returns a tuple of line objects, thus the comma
fig.canvas.draw()
fig.canvas.flush_events()


while 1:
    timestart=time.time()
    data,addr=UDPSock.recvfrom(bytelen)
    p=list(unpack(unpstr,data))
    time.sleep(shitime)
    dwin[0:winlen-shilen]=dwin[shilen:winlen]
    dwin[winlen-shilen:winlen]=p
    line1.set_ydata(dwin)
    
    fig.canvas.draw()
    fig.canvas.flush_events()
    print(time.time()-timestart)

for i in range(int((len(d)-winlen)/shilen)):
    time.sleep(shitime)
    dwin[0:winlen-shilen]=dwin[shilen:winlen]
    dwin[winlen-shilen:winlen]=d[winlen+shilen*i:winlen+shilen*(i+1)]
    line1.set_ydata(dwin)
    fig.canvas.draw()
    fig.canvas.flush_events()
    print("update num:",i)


input()
