import array as a
####### ARRAY ##################
b = a.array('i',[10,20,40,30]) # Here 'i' represent typecode means which type of elemenets in the array
# print(b)
# print(type(b))
# print(b.typecode)
# print(b[3])

## ARRAY OPERATIONS
# b.insert(1,90) # will insert one number at the defined index
# print(b)
# b.append(80) # will add one element at the last of the array
# print(b)
# b.remove(30)
# print(b)

# $$$ INTERATE array elements
# for i in b:
#     print(i,end=" ")

# for i in range(4):
# #     print(b[i],end=" ")
# for i in range(len(b)):
#     print(b[i],end=" ")


n = int(input("Enter the size of array: "))
A = a.array('i',[])
for i in range(n):
    x = int(input("enter the number: "))
    A.append(x)

print(A)
# for i in range(n):
#     print(A[i],end=" ")

# to search element in array
s = int(input("Enter the number you want to search: "))

print("here the result: ",A.index(s))
