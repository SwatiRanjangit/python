# about Identifiers Lowercase or upper case case-sensitive should not start with digits , but it is allowed if an
# identifier start with _(underscore) then it is protected and if there is two underscore at the starting then it is
# private. variable is a named memory location

# ===============Multiple assignments==================
a = b = c = 10

# 1st way of printing multiple assigned values
print(a)
print(b)
print(c)

# 2nd way here seperator is an attribute can be anything u want to use as a seperator in between
# print(a,b,c,sep=",")

# * it is also a multiple assignment
x, y, z = 10, 20, 30
print(x, y, z, sep=":")
# * another way of printing the multiple assigned values using end attribute it will avoid line jump and will print
# in the same line
print(x, end=" ")
print(y, end=" ")
print(z)

# so the actual difference between end and seperator is sep is used normally but not in case of loop but end can be
# normally as well as in case of loop to print the values in the same line
for i in range(10):
    print(i, end=" ")

# DATATYPE: python is a dynamic typed programming language means we do not have to specify the data type at the time
# of variables it will be dynamically converted by the python datatype represent the type of data we are going to
# store inside the variables Basic datatype 1. None = nothing or may be null if we don't want to give any value to
# the variable at that time we use this if that time we don't hve clarity to assign varible. v = None print(type(v))
# 2. Numeric- int, float, bool , complex Type conversion
r = 10.9
print(r)
print(type(r))

n = int(r)  # coverting float to int
print(n)
print(type(n))

# ******************* DATASTRUCTURES ***********************

# 1. string
# 2. List
# 3. Tuple
# 4. Sett
# 5. dict
# 6. range
# 7. bytes
# 8. bytearray
# 9. frozenset

# *INPUT*  is for built-in function to read the values from user
# by default input will take user input as string type so if we want to take input in any other
# data type then we have to specify explicitly

name = input("Enter your name: ")
print("Name is: ", name)
print(type(name))

digit = input("Enter a digit: ")
print("Digit is: ", digit)
print(type(digit))  # here prints type string so if we want int type then

d = float(input("Enter a digit: "))
print("Digit is: ", d)
print(type(d))

# Another example for input takes user input as string
a = input("Enter num1: ")
b = input("Enter num2: ")
a = int(input("Enter num1: "))
b = int(input("Enter num2: "))
sum = a + b
print(sum)  # if we take num1=10 num2=20 print 1020 as + means concatenation in string

# =============== BOOL datatype ==================
# return either true or false depends on condition and in case of
# integer value of true = 1 and false = 0
a = 10
b = 20
c = b > a
print(c)
print(type(c))

# ====================== COMPLEX ===================


# is a combination of real and imaginary part in python "j" is the imaginary part in case of "i"
c = complex(a, b)
print(c)
print(type(c))

print(c.real)  # to extract real part from complex value
print(c.imag)
z = 3 + 4j

# ================== DIR =======================


# - it will print all the related functions of the object passed into it
# print(dir(str)) # in this names started with __name__ is a special type of function called python descriptor
# help -- it can be used to know about any functions in details

# =================1.STRING=====================


# in python str represent string can be created by '' or "" (
# recommended) or ''' ''' or """ """ => tripe quotes can be helpful in case of multiple line string or a paragraphn
# not in case of single word strings are immutable can't be modified directly "" are recommended generally because
# suppose if we are assigning value like durga's software to a string variable we can't able to assign it using '' (
# single quotes) as compiler got confused about single quotes and apostrophe (') int the string and will throw syntax
# error, so we should use ""(double quotes) n = 'durga's'software'  syntax error in this case to diffrentiate it we
# have to use \' n = 'drag\'s software' so better to use "" n = "drag's software"

# TO prove string is immutable as we can take one example s = "python is a easy language" print("Before replacement:
# ",s) s.replace("is","is not") print("After replacement: ",s)   # It will not print the modified string as when we
# use replace function it will return a new string after modification so we need to store the newly created string if
# we want to print or use it that's why we are printing s then it is printing the old value of string


# m = s.replace("is", "is not") print("After replacement: ", m) or also we can do like this print(s.replace("is",
# "is not"))   # this is only used to print the replaced string, but we can not reuse this modified string actually
# here it's basically printing the value returned by replace function

# ===========================2. LIST==============================


# * It is an ordered collection of elements
# * it is created using []
# * allow duplicate and different data type (heterogeneous) collections of elements
# * it is mutable and support index based value

l = [1, 2, 3, 4.5, 10, 6.09, "ram"]
print(l)
l.insert(2, 101)
print(l)

# ===========================3. TUPLE==============================
# * It is an ordered collection of elements
# * it is created using () or without ()
# * allow duplicate and different data type (heterogeneous) collections of elements
# * it is immutable and support index based value
# NOTE: it can not contain one value if one value then it will became simple datatype like int , float

# so create tuple with single element we have to put (,) after the value

l = (1, 2, 3, 4.5, 10, 6.09, "ram")
l = (1,)  # single value tuple
print(l)
l.insert(2, 101)  # give error as it is immutable
print(type(l))

# ===========================4. SET==============================
# * It is an un-ordered collection of unique elements
# * it is created using {}
# * allow different data type (heterogeneous) collections of elements
# * it is mutable
# * there is not any concept of index
# NOTE: to create empty set use set() function

s = {10, 20, 40, 30.5}
print(s)
print(type(s))
p = {}
print(type(p))  # it is not set it is dict (dictonary)

# ===========================5. DICT==============================
# * It is a dictonary, and it is a collection of items and each item can be pair of key and value
# * it is created using {}
# * allow duplicate and diffrent data type (heterogeneous) collections of elements
# * we can't say mutable of immutable about dict as key in dict is immutable and value can be mutable
# * key must be unique, and it can be of any type (int,string,bool etc)

d = {1: "durga", 2: "swat", 3: "ram", 4: "durga"}
d = {1: "durga", "name": "swati", 3.0: 10, 4: "durga"}

# d={(1,2,3): "swati"}  # key is of tuple type as tuple is immutable, so it can be used as key as key must be
# immutable or unique print(d)

# # NOTE: here as a key we can't take list and set as list is mutable but as per key rule key can not be mutable so
# it will give error if we use it d={[10,20]:"swat"} print(d)

# ===========================6. Range==============================
# * It is a used to generate range of values
# * by default it starts with 0
# * it is immutable
r = range(10)
r = range(1, 11)  # start end
r = range(1, 11, 2)  # start end step
print(list(r))
