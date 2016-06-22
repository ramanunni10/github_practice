import threading
from time import sleep
def even():
    x=0
    while 1:
        x=x+2
        print x
        sleep(0.5)
def odd():
    y=1
    while 1:
        y = y+2
        print y
        sleep(0.5)
t1=threading.Thread(target=even)
t2=threading.Thread(target=odd)
t1.start()
t2.start()


