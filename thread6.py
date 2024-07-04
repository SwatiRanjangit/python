from threading import *
import time

def f1():
    print(current_thread().name,"...started")
    time.sleep(1)
    print(current_thread().name,"....ended")


print("number of active thread are: ",active_count())

t1 = Thread(target=f1,name="childThread1")
t2 = Thread(target=f1,name="childThread2")
t3 = Thread(target=f1,name="childThread3")

t1.start()
t2.start()
t3.start()

# print("number of active thread are: ",active_count())
# time.sleep(5)
# print("number of active thread are: ",active_count())

print(t1.name,"is alive ",t1.is_alive())
print(t2.name,"is alive ",t2.is_alive())
print(t3.name,"is alive ",t3.is_alive())
time.sleep(5)
print(t1.name,"is alive ",t1.is_alive())
print(t2.name,"is alive ",t2.is_alive())
print(t3.name,"is alive ",t3.is_alive())
