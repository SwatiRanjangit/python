
# TO ACCESS MODULES FROM THE PACKAGE:
# SYNTAX :
#           import sys
#           sys.append.path("path of the package")

#1.  IMPORT MODULE FROM SINGLE PACKAGE:

import sys
# sys.path.append("C:/Users/Swati Ranjan/PycharmProjects/pythonProject1/package1")

#OPTION 1:
# import module1
# import module2
#
# module1.display()
# module2.show()


#OPTION 2:
# from module1 import *
# from module2 import *
#
# display()
# show()


#2.  IMPORT MODULE FROM SUB-PACKAGE PACKAGE:
# sys.path.append("C:/Users/Swati Ranjan/PycharmProjects/pythonProject1/package1")
# from module1 import *
#
# display()
#
# sys.path.append("C:/Users/Swati Ranjan/PycharmProjects/pythonProject1/package1/package2")
# from module3 import *
#
# showme()

#3.  IMPORT CLASS FROM TWO DIFFRENT MODULES AND PACKAGE:

sys.path.append("C:/Users/Swati Ranjan/PycharmProjects/pythonProject1/package3")
from module1 import *

e = Employee(23,"swati","patna")
e.displayEmp()

sys.path.append("C:/Users/Swati Ranjan/PycharmProjects/pythonProject1/package4")

from module2 import *

s = Student(45,"teesa","up")
s.displayStu()
