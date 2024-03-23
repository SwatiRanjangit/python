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

#TUPLE
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
s = {40,24,40,35};
print(s)
print(type(s))



