ld = open("list_data.txt","w")
l = ["ram\n","mohan\n","shyam\n"]
ld.writelines(l)
print("data is printed")
ld.close()