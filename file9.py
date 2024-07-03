import os

f_name = input("Enter the file name you wanna check: ")

if os.path.isfile(f_name):
    print("file exist ",f_name)
    f = open(f_name,"r")
    print("content of the file:")
    print(f.read())
    f.seek(0) # we have to put this otherwise the cursor after read operation will be at last and
              # we will not able to find line count word count or character count

    l_count = w_count = c_count = 0
    for line in f:
        l_count = l_count+1
        c_count = c_count + len(line)
        word = line.split(" ")
        w_count = w_count + len(word)

    print("No of lines: ",l_count)
    print("No of characters: ", c_count)
    print("No of words: ", w_count)
    f.close()

else:
    print("file not exist ")