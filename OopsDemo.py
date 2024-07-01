#                   OOP'S:
#  security   : only sepcified person can access the program and it's diffrenet for diffrent type of people
#  re-usabilty : reuse to make it better by adding more features into it
#  app-enhancement : by adding more features in the existing program
#    CLASS: collection of variables and methods eg: Bird is a class
#    object: instance of class, represnt the class eg: eagle is object

#                   OOP'S FEATURES:
# encapsulation: process of providing restriction to access varibles and methods from the class
#                  we need it to prevent data from modification by unauthorized person
#                   achieved by making varibles and methods private


# inheritance:creating new class from existing class


# polymorphism: same fucntion with diffrent behaviours means when we change the paramentes it will run diffrently

#               static or compile time------overaloading: when two function name is same but signature is different--------------code refinement  technique
#               dynamic or runtime----------overriding: when two function name and signature is same but implementation is diffrent---------code replacement technique


# abstraction: only show what needed to be shown ..... hiding the actual implementaion and only showing the thing which is useful for the user


# class Employee:
#     def __init__(self):
#         self.eid=123
#         self.e_name="swati"
#         self.e_add="patna"
#     def display_emp_details(self):
#         print("emp id: ",self.eid)
#         print("ename is: ",self.e_name)
#         print("address is: ",self.e_add)
#
# e= Employee()
# e.display_emp_details()
# print(help(Employee))

# print(e.__doc__)  used to print document string of the class

#======================== CONSTRUCTOR ===========================
# it is use to initilaise the value of varibale
# special type of function
# it's name is always __init__(self)
# self is special vvariable in python
# it is first parameter of constructor
# it is used to acess current class members
# it is only used withing the class (not outside the class)
# constructor execute automatically when object is created
# we can create any number of objects and for each object constructor will be execute once
# if we don't define self in the function parameter the first argument is by default made as self


# ==================== METHODS ======================================
# it is reusable piece of code
# self is first parameter of the method
# it will execute when we call it


# ====== Constructor with parameters =========
# class Employee:
#     def __init__(self,id,name,add):
#         self.eid=id
#         self.e_name=name
#         self.e_add=add
#
#     def display(self):
#         print("id: ",self.eid)
#         print("name: ", self.e_name)
#         print("address: ", self.e_add)
#
# e = Employee(23,"riya","patna")
# e.display()


## program to take input from user using fucntion

class Employee:
    def take(self):
        self.eid = int(input("Enter the id: "))
        self.e_name = input("Enter the name: ")
        self.e_add = input("Enter the address: ")

    def display_details(self):
        print("id: ", self.eid)
        print("name: ", self.e_name)
        print("address: ", self.e_add)

e = Employee()
e.take()
e.display_details()





