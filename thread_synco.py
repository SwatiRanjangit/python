from threading import *
import time

# USING  LOCK :

# l = Lock()
# def f1(name):
#     for i in range(10):
#         l.acquire()
#         print("hello gm", end=" ")
#         time.sleep(2)
#         print(name)
#         l.release()
#
#
# t = Thread(target=f1,args=("sai",))
# t1 = Thread(target=f1,args=("swati",))
# t.start()
# t1.start()

# # USING  LOCK PROBLEM DEMO : thread block and will not show any result
#
# l = Lock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#         res = 1
#     else:
#         res = n * factorial(n-1)
#     l.release()
#     return res
#
# def result(n):
#     print("factorial is: ",factorial(n))
#
# t1 = Thread(target=result,args=(3,))
# t2 = Thread(target=result,args=(4,))
# t1.start()
# t2.start()

#USING RLOCK:


# l = RLock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#         res = 1
#     else:
#         res = n * factorial(n-1)
#     l.release()
#     return res
#
# def result(n):
#     print("factorial is: ",factorial(n))
#
# t1 = Thread(target=result,args=(3,))
# t2 = Thread(target=result,args=(4,))
# t1.start()
# t2.start()


#USING SEMAPHORE:

l = Semaphore(3)
def f1(name):
    for i in range(10):
        l.acquire()
        print("hello gm", end=" ")
        time.sleep(2)
        print(name)
        l.release()


t = Thread(target=f1,args=("sai",))
t1 = Thread(target=f1,args=("swati",))
t2 = Thread(target=f1,args=("tiya",))
t3 = Thread(target=f1,args=("sweety",))
t4 = Thread(target=f1,args=("riya",))
t5 = Thread(target=f1,args=("siya",))

t.start()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()