import socket
import threading
from conf_sq import db
from threading import Thread
from time import strftime

s= socket.socket()

s.bind(('192.168.1.12',12345))
s.listen(1)

print "waiting for connect"
c,addr=s.accept()
print "connected"

def send():
	global s
	try:
		while 1:
			tempr=raw_input("server:")
			if tempr =='q':
				break
			dater=strftime("%d-%m-%Y %I:%M:%S")
			#num= 300
			if (int(tempr) > 300 ) or (int(tempr)<0):
				tempr='e'	

			try:
				c.send(dater+","+tempr)
			except Exception, e:
				db.insert_values(dater,tempr)

			  
	finally:
		print "send is closing s"
		s.close()
def rec():
	global c
	try:
		while 1:
			#print "waiting to recieve"
			reply=c.recv(1024)
			if reply =='q':
				break
			elif not reply:
				print ":("
				break 
	finally:
		print "rec is closing s"
		s.close()
t=Thread(target=rec)
t.start()
send()

	 