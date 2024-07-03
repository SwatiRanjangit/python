from zipfile import *
#================== ZIP==================

# f = ZipFile("filezip.zip",'w',ZIP_DEFLATED)
# f.write("sample.txt")
# f.write("sample1.txt")
# f.write("rrr.txt")
# print("zip file created successfully")
# f.close()

# =============UNIZIP==================

f = ZipFile("filezip.zip",'r',ZIP_STORED)
names = f.namelist()
print("all files are: ",names)

for name in names:
    print("file name is: ",name)
    f = open(name,'r')
    print("content of file is: ")
    print(f.read())

f.close()

