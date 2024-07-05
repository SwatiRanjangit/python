#                       PANDAS---Panel data
#----------------------------------------------------------------------------------
# used for data analysis purpose
#return data in form:
# 1. Data series:  single dimension array format
# 2. Data Frame: two dimension array format

from pandas import *
# data = [10,20,30,40,50]
# data = {"a":10, "b": 20,"c":30}
# # s = Series(data)
# s = Series(data,index=['b','c','d','a'])
# print(s)
# print(s[0:2])


# print(Series(10))


# data = [["sai",4],["rohan",3],["tiya",5],["raushan",6]] # List values
# df = DataFrame(data,columns=['name','age'])
# print(df)

# data = {"name": ["swati","sai","tiya","teesa"],"age": [20,24,35,67]}
# df = DataFrame(data)
# print(df)
# print(df.head(1))
# print(df.tail(1))

# df1 = DataFrame([[1,2],[3,4]],columns=['a','b'])
# df2 = DataFrame([[5,6],[7,8]],columns=['a','b'])
#
# df1 = df1._append(df2)
# print(df1)

df1 = DataFrame({"name": ["swati","sai","tiya","teesa"],"age": [20,24,35,67]},index=[1,2,3,4])
df2 = DataFrame({"name": ["riya","sar","kiya","liya"],"age": [22,24,34,98]},index=[5,6,7,8])

df3 = concat([df1,df2])
print(df3)
