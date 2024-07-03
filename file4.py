# f = open("mohan.txt","r")
# data = f.read()
# print(data) # give error as mohan file not exist

f = open("list_data.txt","r")
# data = f.read()
# data = f.read(5)
# data = f.readline()
data = f.readlines()

print(data)