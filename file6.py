f = open("sample1.txt","r")
print(f.tell())
print(f.read(3))
print(f.tell())
f.seek(10)
print(f.tell())
f.close()