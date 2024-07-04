from re import *

mailid = input("Enter the email id : ")

match = fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com",mailid)

# match = fullmatch("\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",mailid) # this is pattern for all kind of mail matching pattern like gmail, yahoo and all


if match != None:
    print("mail id is valid")
else:
    print("mail id is invalid")