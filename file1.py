# f = open("sample.txt","w")
# print("name: ",f.name)
# print("mode: ",f.mode)
# print("is file writable? ",f.writable())
# print("is file readable? ",f.readable())
# print("is file closed? ",f.closed)
# f.close()
# print("is file closed? ",f.closed)

# WRITE OPEARTION IN THE FILE:

# f.write("Hello\n")
# f.write("swati\n")
# f.write("how are you? \n")
# f.write("is everything fine? \n")
# print("data written to the file.")
# f.close()

# APPEND OPERATION IN THE DATA:
f = open("sample.txt","a")
f.write("yea hii\n")
f.write("rashmi\n")
f.write("how do you do? \n")

print("data written to the file.")
f.close()