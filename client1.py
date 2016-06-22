import socket
s= socket.socket()
host='127.0.0.1'
port=12345
s.connect(('127.0.0.1',12345))
while 1:
	reply=s.recv(1024)
	if reply =='q':
		s.close()
		break
	print "server:"+reply 
	x=raw_input("me:")
	s.send(x)
	if x =='q':
		s.close()
		break	

