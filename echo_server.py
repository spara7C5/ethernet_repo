# Echo server program
import socket

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
i=0
while 1:
    #print(i)
    #i+=1
    data = conn.recv(2)
    print(data)
    if not data: 
        print("server breaks the socket")	
        break
    conn.sendall(data)
conn.close()
