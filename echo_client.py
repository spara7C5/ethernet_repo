# Echo client program
import socket
import time

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'HelloHello')
time.sleep(0.1) #time between the sending and the reading:
				# if you receive you cannot send anymore
				#therefore sleep depends of the reading cycle of echo_server=(read+send+...)
data = s.recv(1024) 
s.close()
print('Received', repr(data))
