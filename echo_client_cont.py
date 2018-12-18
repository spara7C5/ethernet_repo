# Echo client program
import socket
import time

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((HOST, PORT)) ### establishing a connection: TCP only
for i in range(10):
	#### characters #######
	#word='HelloWord'+str(i)
	#s.sendall(bytes(word,"utf-8"))

	#### numbers ###########
	s.sendto(bytes("ciao","utf-8"), (HOST, PORT))
#s.close()

