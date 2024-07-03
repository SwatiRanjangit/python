#           ENCAPUSLATION
# ------------------------------------------------------------------
# achieve by making  private methods   or private variables if we want to no one access in the code
# private method: can acessed within the class and if we wnat to access outside we can access by constructor

# class car:
#     def __init__(self):
#         self.__update_software()
#
#   # private method
#     def __update_software(self):
#         print("software update")
#
# c = car()

# class Car:
#     __name = ""
#     __speed = 0
#     def __init__(self):
#         self.__name="grand vitara"
#         self.__speed = 100
#
#         print(self.__name)
#         print(self.__speed)
#
#     def __update_software(self):
#         print("software update")
#
#     def drive(self):
#         print("drive {} with the speed of {} ".format(self.__name,self.__speed))
#
#     def set_speed(self,sp):
#         self.__speed=sp
#
#
#
# c = Car()
# c.drive()
# # c.__speed = 200 # will not change cz speed is private variable so can't modify from outside the class
# # c.drive()
# c.set_speed(200)
# c.drive()

#                           INHERITANCE CLASS
# ------------------------------------------------------------------------
# CREATING NEW CLASS FROM EXISTING ONE
# reusablity and extensiblity

#======= TYPES OF INHERITENCE=========

# single
# multiple
# multi-level
# hybrid
# hierarchial


# SINGLE INHERITENCE EXAMPLE:/


# b = Branch()
# b.get_branch_details()
# b.display_branch_details()

# class Employee(Branch):
#     def get_emp_details(self):
#         self.eid = int(input("enter the employee id: "))
#         self.ename = input("enter the employee name: ")
#         self.eaddress = input("enter the employee address: ")
#
#
#     def display_emp_details(self):
#         print("employee id is: ",self.eid)
#         print("employee name is: ", self.ename)
#         print("employee address is: ", self.eaddress)

# e = Employee()
# e.get_emp_details()
# e.get_branch_details()
# e.display_emp_details()
# e.display_branch_details()

# multi level
# class Employee(Branch):
#     def get_emp_details(self):
#         self.eid = int(input("enter the employee id: "))
#         self.ename = input("enter the employee name: ")
#         self.eaddress = input("enter the employee address: ")
#
#
#     def display_emp_details(self):
#         print("employee id is: ",self.eid)
#         print("employee name is: ", self.ename)
#         print("employee address is: ", self.eaddress)
#
# class EmployeeSalary(Employee):
#     def get_basic_salary(self):
#         self.sal = int(input("enter the basic salary: "))
#
#     def cal_sal(self):
#         self.DA = self.sal * 0.04
#         self.HRA = self.sal * 0.4
#         self.gross = self.sal + self.DA + self.HRA
#
#     def display_salary_details(self):
#         print("DA is: ",self.DA)
#         print("HRA is: ", self.HRA)
#         print("Gross is: ", self.gross)


# e = EmployeeSalary()
# e.get_branch_details()
# e.get_emp_details()
# e.get_basic_salary()
# e.get_branch_details()
# e.get_emp_details()
# e.display_salary_details()


#                   MULTIPLE INHERITENCE (using MRO (method resolution order))
# --------------------------------------------------------------------------------------
# order will be left to right
# class A:
#     def f1(self):
#         print("f1")
#     # pass
#
# class B:
#     def f1(self):
#         print("f2")
#
# class C(A, B):
#     def f3(self):
#         print("f3")

# c = C() # if two class have same function name then the order of execution of that function will be depend on the child
# class inherited order if it is like C(A,B) then A class function will execute and vice versa
# c.f1()
# c.f3()
# c.f2()

#                       POLYMORPHISM
# -------------------------------------------------------------------------------
# static or compile time polymorphism in python:
# 1. operator overloading -- yes
# 2. constructor overloading -- not possible in python
# 3. method overloading -- not possible in python cz python is interpreted language and hence when it starts
# executing the program it will first check the fucntion call if it match then goes down if 3 function having
# same name then the last one will be called and if last fucntion took 2 arguments and we are calling function without
# any arguments then it will throw error


# dynamic or run time polymorphism
#1.  method overriding --yes
# 2. contructor overriding -- yes

#NOTE: in python every operator is having magic methods

# OPEARTOR OVERLOADING EXAMPLE: adding two reference

# class Book:
#     def __init__(self,page):
#         self.page=page
#
#     def __add__(self, other):
#         return self.page+other.page
#
#
# b = Book(30)
# b1 = Book(20)
# print("total book: ", b + b1)

#===================== OVERRIDDING ================
#------------------ Method overriding--------

# class Parent:
#     def assets(self):
#         print("gold , silver, diamond")
#
#     def car(self):
#         print("car ")
#
# class Child(Parent):
#     def jwel(self):
#         print("jwellery is there")
#
#     def car(self):
#         super().car() # in child classs want to access the parent class merthod as well then it can be accessed by using super keyword
#         print("mercedes Benz")
#
# c = Child()
# c.assets()
# c.car()
# c.jwel()


#------------------ Constructor overriding--------
class Parent:
    def __init__(self):
        print("parent class constructor")


class Child(Parent):
    def __init__(self):
        super().__init__()
        print("child class constructor")

c = Child()
