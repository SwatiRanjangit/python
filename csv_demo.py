from csv import *

#========== write data in csv file ===========
# with open("emp.csv",'w') as f:
#     w = writer(f)
#     w.writerow(["eid","ename","eadd","eage"])
#     n = int(input("Enter the number of rows: "))
#
#     for i in range(n):
#         eid = int(input("Enter the id: "))
#         ename = input("Enter the name: ")
#         eadd = input("Enter the address: ")
#         eage = int(input("Enter the age: "))
#         w.writerow([eid,ename,eadd,eage])
#
# print("csv file is created successfully")

#========== read data in csv file ===========

f = open("emp.csv",'r')
data = reader(f)
d = list(data)
# print(list(data))
# for i in d:
#     print(i)

for i in d:
    for r in i:
        print(r,end=" ")
    print()




f.close()
