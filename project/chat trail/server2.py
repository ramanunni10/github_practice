import socket
import threading
from conf_sq1 import db_2
from threading import Thread
s= socket.socket()
host='127.0.0.1'
s.bind(('127.0.0.1',1234))
s.listen(1)
print "waiting for connect"
c,addr=s.accept()
print "connected"

def send():
	global s
	ts_old=0
	try:
		while 1:
			#x=raw_input("server:")
			ds,ts=db_2.read_one()
			if ts_old !=ts :
				#print "not same"
				c.send(str(ds)+","+str(ts))
				ts_old=ts
			else:
				continue

			if str(ts) == 'q':
				break 
	finally:
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
			#print "client:"+reply 
	finally:
		s.close()
		
t=Thread(target=rec)
t.start()
send()
	 

