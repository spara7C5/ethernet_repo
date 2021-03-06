
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

winlen=2000
shilen=200
shitime=0.1 # equal to update time
unpstr='{}f'.format(shilen*3)
bytelen=4*3*shilen
x=range(winlen)
yd=[0 for i in range(winlen)]
yt=[0 for i in range(winlen)]
yf=[0 for i in range(winlen)]

dwin=yd
twin=yt
fwin=yf


# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, =ax.plot(x,yd,'red')
line2, =ax.plot(x,yt,'orange')
line3, =ax.plot(x,yf,'green')

fig.canvas.draw()
fig.canvas.flush_events()

j=0
while 1:
    timestart=time.time()
    data,addr=UDPSock.recvfrom(bytelen)
    p=list(unpack(unpstr,data))
    #time.sleep(shitime)
    dwin[0:winlen-shilen]=dwin[shilen:winlen]
    dwin[winlen-shilen:winlen]=p[0:(3*shilen):3]
    twin[0:winlen-shilen]=twin[shilen:winlen]
    twin[winlen-shilen:winlen]=p[1:(3*shilen):3]
    fwin[0:winlen-shilen]=fwin[shilen:winlen]
    fwin[winlen-shilen:winlen]=p[2:(3*shilen):3]
    line1.set_ydata(dwin)
    line2.set_ydata(twin)
    line3.set_ydata(fwin)
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()
    fig.canvas.flush_events()
    print("data n:",j,"time:",time.time()-timestart)
    j+=1

#for i in range(int((len(d)-winlen)/shilen)):
#    time.sleep(shitime)
#    dwin[0:winlen-shilen]=dwin[shilen:winlen]
#    dwin[winlen-shilen:winlen]=d[winlen+shilen*i:winlen+shilen*(i+1)]
#    line1.set_ydata(dwin)
#    fig.canvas.draw()
#    fig.canvas.flush_events()
#    print("update num:",i)


