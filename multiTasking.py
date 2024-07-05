#                   MULTI TASKING
#=============================================================================
# TWO TYPES:
# 1. Process based multi-tasking (multi-processing, OS Level): execute several tasks simulteniosuly and each process will execute seperatly
# 2. Thread based multi-tasking (multi-threading): execute several tasks simulteniosuly and each task will execute independatly part of the same program
#                                       used in: multi media graphics, animations , video games etc


#                   MULTI THREADING
#=============================================================================
# import threading
# every python by default contain one thread which is main thread
# 3 ways to create Threads in python
# 1. create thread without using any class
# 2. create thread by extending thread class
# 3. create thread without extending thread class

# MTHODS:
#1. active_count(): return number of threads running currently
#2. is_alive(): used ot check thread executing currenlty or not
#3. join(): if thread wants to wait until completing some other thread

#                    THREADS SYNCHRONIZATION
#=============================================================================
# USING this we can achieve synch

#1. LOCK :
#2. RLOCK:
#3. SEMAPHORE:

#1. LOCK :
#           Create lock  object:
# l=lock()
#Lock can be hold by only one thread at a time if any other thread require the same lock it has to wait
#until relase the lock
# thread can aquire lock using acquire() method eg: l.acquire()
# thread can release lock using release() method eg: l.release()
# PROBLEM WITH LOCK:
#       it doesn't know which thread is acquiring lock and if a thread acquire lock and then any other thread try to acquire that lock then
#       it will block thread cz it dosen't know which one is acquirinth lock

# NOTE: to call release method thread should be owner of that lock (thread shiuld have that lock)

#2. RLOCK: Rentrant Lock
# iprovement of Lock
# same thread which acquired the lock the that thread can acquire lock any time
# but if other thread try then it will block those thread
# it has info which thread acquired lock or not

#3. SEMAPHORE:
# when we want to lock aquire by more than one thread then we use semaphore
# as with use of lock and rlock oly one thread can acquire lock at the time
# s= Semaphore(counterpart) by default counterpart=1 and it can as many as user want that number of threads execute at a time
# every acquire method counterpart is increase by 1
# every release method counterpart is decreased by 1
# in noram semaphore we can call any number time release method and it will increase accquire emthod wheter it is not required
# so we use bounded semaphore it will probhit from this type of prgamatic mistake.both acquire adn release will called same time

# s = BoundedSemaphore(3)
