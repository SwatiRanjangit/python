import time
from threading import *


# SINGLE THREAD PROGRAM
# def square(num):
#     for n in num:
#         time.sleep(1)
#         print("square is : ",n*n)
#
# def cube(num):
#     for n in num:
#         time.sleep(1)
#         print("cube is : ",n*n*n)
#
# num = [2,3,4,1]
# t = time.time()
# square(num)
# cube(num)
# print("time is: ",time.time()-t)


# MULTI THREAD PROGRAM

def square(num):
    for n in num:
        time.sleep(1)
        print("square is : ", n * n)


def cube(num):
    for n in num:
        time.sleep(1)
        print("cube is : ", n * n * n)


num = [2, 3, 4, 1]
r = time.time()
t1 = Thread(target=square, args=(num,))
t2 = Thread(target=cube, args=(num,))
t1.start()
t2.start()

t1.join()
t2.join()

print("time is: ", time.time() - r)
