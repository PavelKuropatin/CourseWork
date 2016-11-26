import threading
import datetime
def t1(i,*args):
    while i:
        print("thread1 - ",i,' ', datetime.datetime.now())
        i-=1

def t2(i, *args):
    while i:
        print("thread2 - ",i,' ', datetime.datetime.now())
        i-=1
i=100
th1 = threading.Thread(target=t1, args=(i,i,i,i))
th1.start()
th2 = threading.Thread(target=t2, args=(i,i,i,i))
th2.start()