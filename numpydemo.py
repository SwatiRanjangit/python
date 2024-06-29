from numpy import *
# l = array([10,20.0,30,40,50])
# l = array([10,20.0,30,40,50],dtype=int)
# print(l)
# print(l.ndim) # print dimesion of the array
# print(l.dtype) # print datatype of elements
# print(l.shape)

# print(linspace(2,20,9)) # it will divide 2 to 20 in total 9 parts (start,stop,increment)
# print(arange(2,20,2)) print the number in range 2 to 20 with increment of 2 values (start,stop,increment)
# A = zeros(10,int)  will print array with 10 zero default datatype is float
# print(A)
# A = ones(10,int)   will print array with 10 one default datatype is float
# print(A)


A = array([[1,2,3],
          [4,5,6],
          [7,8,9]]
          )

print(A)
print(A.ndim)
print(A[1][2])
print(A.shape)
