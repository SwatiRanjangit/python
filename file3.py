# f = open("sample.txt","x") # already created file give FileExistsError error so use try except block to handle these type o scenerio
# f.write("hello")
# print("data writted to file")
# f.close()

try:
    f = open("sample.txt", "x")
    f.write("hello")
    print("data writted to file")
    f.close()
except Exception as msg:
    print(msg)



