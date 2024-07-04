from threading import *

# 2. create thread by extending thread class
# step1: we have to extend the class from Thread class
# step2: override the run method of Thread class compulsory
# step3: whenever we call start() run method will called autometically and perform required task



class Test(Thread):
    def run(self):
        for i in range(5):
            print("child thread")

t = Test()
t.start()

for i in range(5):
    print("main thread")