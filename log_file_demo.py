from logging import *

basicConfig(filename='mylog.txt',level=INFO)
info("A new message request")

try:
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print("result is: ",a/b)

except ZeroDivisionError as msg:
    print("can't divide ",msg)
    exception(msg)

except ValueError as msg:
    print("Enter int values only ")
    exception(msg)

info("Request processed completly")

