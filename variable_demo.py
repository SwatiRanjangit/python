#=============== VARIABLES AND IT'S TYPE ==========================
# instance variable (object) : value vary from object to object
# local variable (method level):
# static variable(class level)

#============= INSTANCE VARIABLE===============================
#  instance variable (object) : value vary from object to object
# declare inside constructor and method using self
# declare outside the class using slef refrence
# access inside the class using self
# access outside the class using object refrence
# *****NOTE: We can create any number of objects of the class and for each class
# and for every object seperate copy of instance varible will be called
# changes of any perticular value of instance in the object doesn't affect others

# Delete inside the class using del self.variablename
# delete outside the class using object refrence del objectRefernce.variablename



# class demo:
#     def __init__(self):
#         self.a = 10
#         self.b = 30
#
#     def delete_variable(self):
#         del self.b
#
# d = demo()
# d1=demo()
# print(d.__dict__)
# print(d1.__dict__)
#
# # d1.delete_variable()  deleting only d1 instance variable using delete funtion
# print(d.__dict__)
# print(d1.__dict__)
# d.c=20 way of declaration of instance variable outside the class
# print(d.__dict__)


#================== STATIC VARIABLES ===================

# value of variable not vary object to object
#declare inside the class but ooutside of any methods
# for all object there is only one copy of static varible will be created
# hence changes made will be reflected

# class test:
# #     a = 110 # static variable
# #     def __init__(self):
# #         self.b=40  # it is instance varible . always associated with self keyword
# #
# # t = test()
# # t1 = test()
# # print(t.a,t.b)
# # print(t1.a,t1.b)
# #
# # test.a=50 # changing the static variable value using class name
# #
# # print(t.a,t.b)
# # print(t1.a,t1.b)

#=================== LOCAL VARIABLE ==========================
# declared inside the method and only accessed within that perticular method
# as soon as the mehtod execution start those variable will be created
# and when the execution end those varible will be distroyed
