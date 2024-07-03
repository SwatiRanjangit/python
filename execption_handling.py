#                   Exception Handling Mechanism
#------------------------------------------------------------------------------
# unexpected or unwanted event occur during the execution of program harmful for the flow of program
# syntatical error: wrong spelling to the syntax. not harmful for program as it can be identified by the programming at the time of program compilation
# runtime error: it raise during program execution .. also called exceptions and it will called abnormal termination of program execution
#                  so we need to handle it at the time of programming

#       1. Logical Implementation
#       2. Try except Implementation

#----- TYPES OF EXCEPTIONS -----------
# 1. User defined execptions
# 2. predefined execptions

# NOTE: IN PYHTON EACH EXCEPTION IS A CLASS
# NAME error , Value error, fileNotFound error, ZeroDivision error : BUILT IN exception

# LOGICAL IMPLEMENTATION: all execption will ot be handle using this type

# a = int(input("enter a : "))
# b = int(input("enter b : "))
#
# if b == 0:
#     print("second number can't be zero")
# else:
#     c = a/b
#     print("result is: ", c)

# TRY EXPECT BLOCK
# TRY block is always associated with either except or finally block if not show error
# for each TRY block there could be any number of except block but only ONE finally block
# Exept block has types:
#   Default expect block: except block without any exception class
#   Specific except block: except block with any exception class
# if we are using specific and default both exception in a program then default exvcept should be at LAST only
# and parent specific except class should be at last as well

# FINALLY BLOCK
# mandatory code  if exist any execption this block will be exceuted always
# no matter try or except block exceuted or not

# once control goes inside try blockk then only Finalyy block will be executed

# a=10/0
# try:
#     print("try")
# finally:
#     print("final")

# generally clean up , connection closing code written in FINALLY Block
### NOTE: There is only one situtaion where we can stop finally block exceution that is
#           os._exit(0)  after this PVM(python virtual machine) will shut down itself and finally block will stop executing


# try:
#     a = int(input("enter a : "))
#     b = int(input("enter b : "))
#     c = a/b
#     print("result is: ",c)
# except Exception as msg:
#     print(msg, " error")

# ways of declaring mulitple execption output msg
# except (ZeroDivisionError,ValueError) as msg:
#     print("something went wrong! please check again.: ", msg)

# except ValueError as msg:
#     print(msg," error")


# try:
#     a= 10/0
#     a = int(input("enter a : "))
#     b = int(input("enter b : "))
#     c = a/b
#     print("result is: ",c)
# except Exception as msg:
#     b = 20/0
#     print(msg, " error")
# finally:
#     print("always execute")

# NESTED TRY AND EXCEPT BLOCK IMPLEMENATION
# try:
#     a = 10/0 # will not eceute inner try execept if got exception in outer try bock then control goes to outer except block and finally block
#     print("outer")
#     try:
#         a = 10/0
#         print("inner")
#     except:
#         print("inner except")
#     finally:
#         print("inner finally")
#
# except:
#     print("outer except")
# finally:
#     print("outer finally")

