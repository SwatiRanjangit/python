from re import *

n = input("Enter the mobile number: ")

match = fullmatch("[6-9]\d{9}",n)

if match != None:
    print("phone number is valid")
else:
    print("phone number is invalid")