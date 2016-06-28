import socket
s= socket.socket()
host='127.0.0.1'
port=12345
s.bind(('127.0.0.1',12345))
s.listen(1)
c,addr=s.accept()
while 1:
	data=raw_input("server:")
	c.send(data)
	if data =='q':
		s.close()
		break
	reply=c.recv(1024)
	if reply =='q':
		s.close()
		break
	print "client:"+reply 