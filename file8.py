import os

f_name = input("Enter the file name you wanna check: ")

if os.path.isfile(f_name):
    print("file exist ",f_name)
    f = open(f_name,"r")
    print("content of the file:")
    print(f.read())
    f.close()
else:
    print("file not exist ")