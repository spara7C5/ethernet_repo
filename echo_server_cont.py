# Echo server program
import socket
import time

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ### TCP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ### UDP
s.bind((HOST, PORT))
#s.listen(1) ### num of connections: for TCP only!
#conn, addr = s.accept() ### client recognition: for TCP only!
#print('Connected by', addr)  ### client recognition: for TCP only!
r=[]
while 1:
    #data = s.recv(10)
    data=s.recvfrom(10)
    print(data)
    r.append(data)
    time.sleep(1)
    if not data: 
        print("server breaks the socket")	
        break
print(r)
s.close()
