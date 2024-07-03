data=" this is durgasoft video"
f = open("rrr.txt","w")
f.write(data)

with open("rrr.txt","r+") as f:
    print("current cursor position: ",f.tell())
    text = f.read()
    print(text)
    print("current cursor position: ", f.tell())
    f.seek(7)
    print("current cursor position: ", f.tell())
    f.write(" very good ")
    f.seek(0)
    t = f.read()
    print("after modification data: ")
    print(t)


