
from threading import *
import time

def f1():
    for i in range(5):
        print("child")
        time.sleep(1)

t = Thread(target=f1)
t.start()

t.join(3) # this will executed by main thread if time given in join(time) will greater than the child thread takes time then main thread
#           will not wait for that much time it will start execution just after child thread stops

for i in range(5):
    print("main thread")