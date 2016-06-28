import socket
import threading
from threading import Thread
s= socket.socket()


port=12345

s.connect(('127.0.0.1',12345))

def recieve():
	global s
	try:
		while 1:
			#print "waiting to recieve"

			try:
				reply=s.recv(1024)
			except Exception, e:
				reply = 0
				print 'send: ', e
			
			if reply =='q':
				#s.close()
				break
			elif not reply:
				print "("
				break
			print "server:"+reply 
	finally:
		print "finally block"
	s.send('q')
	print "recieved"

def send():
	global s
	try:		
		while 1:
			#print "waitinig to send"
			x=raw_input("me:")
			
			if x =='q':
				try:
					s.send('q')
				except Exception, e:
					print 'send: ', e
				
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