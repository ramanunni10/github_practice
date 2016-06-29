import socket
import threading
from conf_sq1 import db
from threading import Thread
s= socket.socket()

flag=True
port=12345

s.connect(('127.0.0.1',12345))

def recieve():
	global s,flag
	try:
		while flag:
			#print "waiting to recieve"

			try:
				reply=s.recv(1024)
				t,x=reply.split(',')
				db.insert_values(t,x)
		
			except Exception, e:
				reply = 0
				print 'send: ', e
			
			if reply =='q':
				flag=0
				break
			elif not reply:
				print "("
				flag=0
				break
			print "server:"+reply 
	finally:
		print "finally block"
		#s.close()
	s.send('q')
	print "recieved"
def send():
	global s,flag
	try:		
		while flag:
			#print "waitinig to send"
			x=raw_input("me:")
			
			if x =='q':
				try:
					s.send('q')
				except Exception, e:
					print 'send: ', e
				flag=0
				#s.close()
				break
			s.send(x)
	finally:
		print "finally block"
		#s.close()
	print "send"
t=Thread(target=recieve)
t.start()

send()	
s.close()