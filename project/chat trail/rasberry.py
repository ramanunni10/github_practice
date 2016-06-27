import socket
import threading
from threading import Thread
s= socket.socket()
host='127.0.0.1'
port=12345
s.bind(('127.0.0.1',12345))
s.listen(1)

print "waiting for connect"
c,addr=s.accept()
print "connected"

def send():
	global s
	while 1:

		x=raw_input("server:")
		c.send(x)
		if x =='q':
			s.close()
			break 
def rec():
	global c
	while 1:
		#print "waiting to recieve"
		reply=c.recv(1024)

		if reply =='q':
			s.close()
			break
		elif not reply:
			print ":("
			s.close()
			break
		print "client:"+reply 

t=Thread(target=rec)
t.start()
send()
	 

