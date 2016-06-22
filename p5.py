from time import sleep
import threading
n='a'
def check():
	global n
	while 1:
		n = raw_input()
		if n=='k':
			break
def hello():
	global n
	while n!='k':
		print "hello world"
		sleep(0.5)
		
t1=threading.Thread(target=hello)
t2=threading.Thread(target=check)
t1.start()
t2.start()

