
from threading import *
# 3. create thread without extending thread class

class Test:
    def f1(self):
        for i in range(5):
            print("child")

t = Test()
t1 = Thread(target=t.f1())
t1.start()



