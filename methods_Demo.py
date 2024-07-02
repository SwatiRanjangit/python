#================= TYPES OF METHODS =====================
# instance methods
# class methods
# static methods

                # INSTANCE    METHODS
# ----------------------------------------------------------------------------
# inside method implementation when we use instance variable then that method is called instance method
# while declaring instance method we should pass self
#  self is the first parameter of instance methods
#  using self we can access instance variable inside instance mthods
# we can access instance method inside the class using self.method_name()
# we can access instance method outside the class using object_reference eg: object_name.method_name()
# NOTE: by default all methods in python OOPS is instance methods


# class student:
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self): # instance method
#         print((self.m1+self.m2+self.m3)/3)
#
# s = student(5,5,5)
# s.avg()


#                       CLASS METHODS
#------------------------------------------------------------------------------------

# very rarely used classes in python
# inside method implimentation when we only use static of class variable
# while declaring class methods we should pass class variable i.e cls (name of cls is optional can take any name)
# cls is 1st parameter of class methods using cls we can access static or class variable inside the method
# in python of making any method class method we use @classmethod decorator
# can access class method using classname or object_refrence_name


# class student:
#     scl="durgasoft" #static or class level variable
#
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self): # instance method
#         print((self.m1+self.m2+self.m3)/3)
#
#     @classmethod
#     def m1(cls):
#         print(cls.scl)
#
#
# s = student(5,5,5)
# s.avg()
# student.m1()



#                       STATIC METHODS
#------------------------------------------------------------------------------------
# these methods are general use methods
# we can create these methods according to our requirement
# create this methods no need to pass self or cls as a 1st parameter
# to make a method a static method we use @staticmethod decorator
# we can access static method wither by using class name or object refrence



# class student:
#
#     scl="durgasoft" #static or class level variable
#
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def avg(self): # instance method
#         print((self.m1+self.m2+self.m3)/3)
#
#     @staticmethod
#     def m1(a,b):
#         c = a + b
#         print("this is a static method", a+b)
#
#
# s = student(5,5,5)
# s.avg()
# student.m1(4,4)

#               ==== Where we can access static variables ======

# inside constructor using self or classname
# inside class methods using cls or classname
# inside instance variable using self or classname
# inside static method using classname only
# outside the class by using object refrence

#===== DELETION =========
# we can delete static class anywehere by using the syntax
#              del class_name.variable_name

class student:

    a=10 #static or class level variable

    # constructor
    def __init__(self):
        print(self.a)
        # del student.a  #once we delete the static method then below that we can't use it beacuse python is interprated lang
                         # so below constrictor we will not able to use static variabel a but in constructor we can use
        

 # instance method
    def m1(self):
        print(self.a)
        print(student.a)

    @classmethod
    def m2(cls):
        print(cls.a)
        print(student.a)

    @staticmethod
    def m3():
        print(student.a)


# implementation of where and how we can access static methods

s = student()
s.m1()
s.m2()
s.m3()
print(s.a)



