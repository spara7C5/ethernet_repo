import matplotlib.pyplot as plt
from socket import *
import numpy
import pickle
from struct import unpack


def init_plot():
    global plot,fig,ax
    plt.ion()
    fig, ax = plt.subplots()
    plot = ax.scatter([], [])
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    



def init_socket():
    global UDPSock,buf
    # Set the socket parameters
    host = "localhost"
    port = 10000
    buf = 10240
    addr = (host,port)

    # Create socket and bind to address
    UDPSock = socket(AF_INET,SOCK_DGRAM)
    UDPSock.bind(addr)
    print("socket initialized")
if __name__ == '__main__':
    init_plot()
    init_socket()
    d=[]
    t=[]
    p=[]
    x=1
    while 1:
        data,addr = UDPSock.recvfrom(4)
        p=unpack('f',data) 
        array = plot.get_offsets()
        array = numpy.append(array, numpy.array([x,p[0]]))
        x+=1
        plot.set_offsets(array)
        fig.canvas.draw()
    UDPSock.close()




