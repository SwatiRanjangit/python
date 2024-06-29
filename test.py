import numpy
# print("Hello ghr aa gye wapis")
# print("haa aa gyi")
#
# i = 100
# if i == 10:
#     print("true")
# else:
#     print("false")

# name = input("Enter your name: ")
# print("your name is ", name)
# print(type(name))

# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# sum = num1+num2
# print(sum)

# a = 5
# b = 4
# c = complex(a , b)
# print(c)

# s = "durgasoft's"
# print(s)
# print(dir(str))


# for multiline statement we can use """ in a string
# s = """ swati
# ranjan
# bihar
# """
#
# print(s)

# string is immutable proof:
# s = "python is very easy lang"
# print(s)

# s.replace("is","is not")  # here replace function will do modification , and it returns a new string rather than changing in existing one
# print(s) # so here if we want to print it will print the former string without modification .

# if we want to do modifiaction then we need to store the new string returned by replace function and then use it

# st = s.replace("is","is not")
# print(st)

# there is one another way also
# but the diffrence between this way and above is in here we are not storing the result of the replace function
# ,but we are directly printing the string which is returned by replace func , we can't use it further in the code
# but in above we are storing the value of ,modified string , we can use it further in the code
# print(s.replace("is","is not"))

# LIST
# it is ordered collections of elements
# it can be created using []
# it can stored duplicate values
# can store heterogenous values
# it is mutable(Can change)
# l = [10, 20, 30.4,"swati"]
# print(l)
# print(type(l))
#
# l.remove(10)
# print(l)
# l.insert(1,23)
# print(l)

# TUPLE
# it is orderd collections of elements
# it can be created using () (but () is optional) we can create using ,(Comma)
# it can stored duplicate values
# can store heterogenous values
# it is immutable(Can not change)
# we can't create tuple with one element rather if we want to create then we have to put comma after the element
# l = 10,
# print(l)
# print(type(l))

# SET
# it is un-ordered collection of unique elements
# as it is unordered , it has no indexes here
# it is mutable
# it can have diff datatype
# we create set using {}
# for empty set we use set() function
# s = {40,24,40,35,"swati"};
# print(s)
# print(type(s))

# MEMEBERSHIP operator  EXAMPLE - used to check elements present in sequence or not
# s = [1, 2, 3, 4, 3]
# print(10 not in s)
# IDENTITY Operator : it will check wheteher two variable having same indetity or value
# is and is not is the operator
# id() is a function which return unique address of a varible in the memory location
# s= 10
# p=20
# print(s  is not p)

# CONTROL FLOW STATEMENT
# IF ELSE statement
# i = 10
#
# if i == 100:
#     print('true')
# else:
#     print("false")

# i = int(input("enter a number: "))

# if i % 2 == 0:
#     print(i,"even")
# else:
#     print(i,"odd")

# LOOP (FOR LOOP: when the no of iteration is known and it's has limited iteration we use it )

l = [10, 20, 30, 40]
c = ['a', 'b']
# for i in l:
#     print(i, end=" ")
#     for j in c:
#         print(j,end=" ")
# for i in range(1, 11):
#     print(i, end=" ")
#     if i == 5:
#         break

# for i in range(1, 11):
#     if i == 5 or i == 7:
#         continue
#     print(i, end=" ")

# WHILE LOOP: used when no of iteration is not known and it is in big amount
i = 1
# while i <= 10:
#     print(i, end=" ")
#     i += 1
# while i <= 10:
#     if i == 5:
#         i += 1
#         continue
#     print(i, end=" ")
#     i += 1
s = "durgasoft"
# print(s[0:8:3])
# print(s[:2:-1]) # it will reverse the string
# print((s+" ")* 3) # it will print durgasoft 3 times

#######  STRING SPLIT #############
s = "durga soft is very is good plateform is to learn python"
# s1= s.split(" ")
# print(s.split(" "))
# print(s1) # give output in the list format (return type of SPLIT is LIST)
# for i in s1:
#     print(i)

#### STRING COUNT #####
# sub = "is"
# print(s.count(sub))

####### STRING JOIN ######
# print("#".join(["ram","siya","kiya"]))
# print(" ".join("siya"))

# reverse string using join in this case we can reverse the string and also concate other string with it
# s1= "".join(reversed("swati"))
# print(s1)

######## STRING SORT ########

# s = "pyhton is very good"
# s1= s.split(" ")
# s1.sort()
# print(s)
# print(s1) # it will give acending order result


# s1.sort(reverse=True)
# print(s1)
# for i in range(0,len(s)):
#     for j in range(0,len(s1)):
#         print(s1[::-1])


############## STRING PARTITION ###############
# s = "pyhton is very good language"
# s1 = s.split(" ")
# print(s1)
# print(type(s1))
# s2 = s.partition(" ")
# print(s2)
# print(type(s2))


# ######### program to print reverse of each string in senetence #########
# s= "python is very good"
# ### output: nohtyp si yrev doog
# s1 = s.split(" ")
# for i in s1:
#     print(i[::-1],end=" ")

######### program to remove duplicate characters string in senetence #########
s = "aabbbabababcccc"
# l=""
# for i in s:
#     if i not in l:
#         l=l+i
#
#
# print(l)

# print("".join(sorted(set(s))))  ## will give unique elements after remove duplicates


########### LIST ##############
# l = [1,2,[3,4],5,6,"sai"]
# print(l[2][0])

# LIST COPY : DEEP AND SHALLOW
# SHALLOW

# l=[1,2,3]
# l1 = l
# print(l)
# print(l1)
# l.remove(3)
#
# print(l)
# print(l1)

# DEEP
# l1=l.copy()
# print(l)
# print(l1)
# l1.append(10)
# print(l)
# print(l1)


##### TAKE INPUT FOR LIST FROM USER $$$$$$$$$$$$$$$$

# n = int(input("enter number of elements for the input: "))
# lst=[]
# for i in range(n):
#     ele=int(input("enter the elemnt: "))
#     lst.append(ele)
#
# print(lst)

# $$$$$$$$$$$$$ STRING/LIST INTO TUPLE $$$$$$$$
# L=[10,"Swati",10.4,78,547,8]
# print(l)
# print(type(l))
# t = tuple(l)
# print(t)
# print(type(t))

####### TUPLE PACKING UNPACKING
# PACKING
a = 10
b = 20
v = 30

# t = a,b,v
# print(t)
# print(type(t))

# t = [a,b,v] # due to [] bracket it is list packing
# print(t)
# print(type(t)) ## LIST packing

# UPACKING
# t=(10,20,30)
# a,b,c = t
# print("a= ",a)
# print("b= ",b)
# print("c= ",c)


###################################### SET DATA STRUCTURE #######################
# s = {10,20,10,"sai",10.34,89}
# print(s)
# s.add(30) # add one ele at a time
# print(s)
# s.update(["swati","op",100]) # add multiple ele atr a time
# print(s)
# print(s)

########## DICT ##############
# d = {"name": "swati", "age": 20, "salary": 10000}
# print(d)
#
# print(d["name"])
# print(d.get("age"))
#
# d["name"]="ranjan"
# d["city"]="up" ### ADD this new key value in the dic ct
#
# print(d)

# # DELETE
# del d["name"]
# print(d)

## SECOND LARGEST ELEMENT FROM LIST PROGRAM
l = [30, 20, 1, 78, 54]
# l.sort()
#
# print(l[-2])

## LARGEST ELE IN LIST
# la=l[0]
# for i in l:
#     if i > la:
#         la=i
#
# print("largest number is : ",la)


######### PROGRAM TO PRINT SUM AND AVERAGE
# l = [1,2,3,4,5]
# sum=0
# for i in l:
#     sum+=i
#
# print("Sum is: ",sum)
#
# avg = sum/len(l)
# print("average is: ",avg)

######## program to convert two list into dict
# key=[1,2,3]
# value=["ram","mohan","sohan"]
# d={}
# for i in range(0,len(key)):
#     d[key[i]]=value[i]
#
# print(d)

############ FUNCTION IN PYTHON $$$$$$$$$$$$$$$$$
# def fun1(name): # function defination
#     print("hello! ",name)
#
# fun1("mohan")  # function call

### MULTIPLE VALUE returning from the function
# def add(a,b):
#     sum = a + b
#     sub = a - b
#     return sum,sub
#
# x,y = add(20,10) ## 1. positional argument
# print("sum is: ",x)
# print("sub is: ",y)

# This is not a good apporach as if we assign two or more function to one function then whenever
# we call the function it will perform all the task but if we want only one task to perform that will not be performed
# so it is not a good practice to assign more than two tasks to any function


##2. KEYWORD ARGUMENT: here actual argument is sent with name of formal argument
## hence in this ORDER doesn't matter
# def f1(name,age):
#     print("hello! ",name, age)
#
# f1(age="30",name="swati") # keyword argument
# f1("swati",age=30) # positional argument
# NOTE: we can work with one positional and one keyword argument but positional should be first then keyword

##3. DEFAULT ARGUMENT
# def f1(course="python"):
#     print(course)
# f1()
# f1("science")

## 4. VARIABLE LENGTH ARGUMENT : storage format of variable length argument is TUPLE
# def f1(*n):
#     print(n+n)
#
# f1(10)
# f1(10,20)
# f1(10,20,30,40,50)

# program sum of variable length arugument
# def f1(*args):
#     s=0
#     for i in args:
#         s+=i
#     print(s)

# OR
# def f1(*args):
#    print(sum(args))
#
# f1(10)
# f1(10,20)
# f1(10,20,30,10)

# &&&&&&&& **kwargs: default collection is dict ...variable length keyword argument is passed using this
# def f1(**kwargs):
#     for k,v in kwargs.items():
#         print(k,"=",v,end=" ")
#
#
# f1(a=10,b=20,c=30)
# f1(name="swati",age=20,salary=10000)

############# LAMBDA FUNCTION : function without name, used with filter , map, reduce $$$$$$$$$$$$$$$$$$$$$

# add = lambda a:a+10
# print(add(10))

# add = lambda a,b:a+b
# print(add(10,20))
# add = lambda a,b=20:a+b
# print(add(10))

### FILTER FUNCTION
# without lambda
# ages = [5,12,16,19,37,2,33]
# def my_fun(x):
#     if x < 18:
#         return  False
#     else:
#         return True
#
# adults = list(filter(my_fun,ages))
#
# for x in adults:
#     print(x,end=" ")

##### with lambda
# ages = [5,12,16,19,37,2,33]
#
# adults = filter(lambda a: a>18 , ages)
# for x in adults:
#     print(x,end=" ")

####### MAP WITH LAMBDA
# ages = [5,12,16,19,37,2,33]
# def my_fun(x):
#     if x < 18:
#         return  False
#     else:
#         return True
#
# adults = list(filter(my_fun,ages))
# for x in adults:
#     print(x,end=" ")
# def my_fun1(x):
#     return x * x
#
# square = list(map(my_fun1,adults))
# print("\nafter map result: ")
# for x in square:
#     print(x,end=" ")

############# REDUCE WITH LAMBDA
# from functools import reduce
#
# l = [1,2,3,4,5,6]
# def my_fun(x,y):
#     return x+y
#
# res = reduce(my_fun,l)
# print(res)

## FUNCTION ALIASING
# def f1():
#     print("hello")
#
# f2=f1 # alias

# del f1
# f1()
# f2()
# print(id(f1))
# print(id(f2))

## NESTED FUNCTION
# def f1():
#     print("hello")
#     def f2():
#         print("hi")
#         def f3():
#             print("welcome")
#
#
#         f3()
#     f2()
# f1()


##### RECURSION
# def factorial(n):
#     if n == 0:
#         res = 1
#     else:
#         res = n * factorial(n-1)
#     return res
#
# print("factorial is: ",factorial(3))
#
# from math import *
#
# print(factorial(3))
# print(sqrt(2))
# print(pow(2,2))
# print(sin(0))

