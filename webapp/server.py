import socket
from conf_sq import db
from time import strftime

s=socket.socket()
s.bind(("127.0.0.1",1234))
s.listen(1)
cl,ipc=s.accept()
while(1):
	rec=cl.recv(1024)

	if rec=='q':
		s.close()
		break
	t=strftime("%d-%m-%Y %I:%M:%S")
	db.insert_values(t,rec)

s.close()