import warnings
warnings.filterwarnings('ignore',category=DeprecationWarning)
from threading import *
# print(threading.current_thread().name)
# print(threading.current_thread().getName())
current_thread().name = "sampletherad"
print(current_thread().name)