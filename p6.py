import threading
from threading import Lock
from time import sleep
from random import randint
lock= Lock()
def even():
    global lock
    x=0
    while 1:
        lock.acquire()
        x=x+2
        print "even"
        s=randint(1,5)
        sleep(s)
        lock.release()
def odd():
    y=1
    global lock
    while 1:
        lock.acquire()
        y = y+2
        print y
        s=randint(1,3)
        sleep(s)

        lock.release()
t1=threading.Thread(target=even)
t2=threading.Thread(target=odd)
t1.start()
t2.start()


