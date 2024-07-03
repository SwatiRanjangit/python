#                           FILE HANDLING
#------------------------------------------------------------------------------------
# STORAGE AREA'S: store out data permanently , we use so that we can use it  for later purpose
#   Temporary storage: python objects like: list, tuples, set, dict
#   permanenet storage: files or Databases


#       TYPES OF FILES
#1. Text file: use to store character data(.txt)
#2. Binary file: use to store binary data (images,audio and video)

# Files are use to perform read(output) or write(input) opeartion
# 1. create file using syntax: fileObjectName = open("filename.txt", "filemode")
#           eg: f = open("myfile.txt","w")

#2. Close the file: fileObjectName.close() eg: f.close()

#=======FILE MODES=========
# 1. w --- Write: open existing file for write operation if the name not present then it will create new file with that name and perform write operation
# 2. r --- Read: open existing file for read operation if the name not present then will show FileNotFound Error. this is default mode.
# 3. a --- Append: open existing file for append operation. it won't override the data in the file. if the specified file not exist then it will create a new file and append data into newly file
# 4. x --- exclusive creation for write opeartion: if the file exist already then will show FileExist Error
# 5. w+ --- write and read: it will override the existing data.
# 6. r+ --- read and write: first read then write oepration, The previous data in the file not deletd. file pointer placed at the begining of the file.
# 7. a+ --- append and read: won't override the existing data

#========= FILES PROPERTIES AND METHODS=======
# 1. name: name of the provided file
# 2. mode: mode of the file
# 3. writable(): True/False
# 4. readable(): True/False
# 5. closed: True/False

#========= WRITE DATA INTO FILE==============
# 1. write():
# 2. writelines():

#========= READ DATA INTO FILE==============

# 1. read(): read complete data from file
# 2. read(n): read n no of characters from file
# 3. readline(): read 1st line of file
# 4. readlines(): to read all line into list


#========= WITH STATEMENT==============
# it is used while opening the file to group all the file
# operation statement within a block
# after completing all the file opeartion autometocally file will be closed

#                           FILE MODIFICATION
#------------------------------------------------------------------------------------
# 1. tell(): is used to know the cursor(file pointer) current position
# 2. seek(): is used to move the cursor(file pointer) desired position

#========= CHECK IF FILE EXIST OR NOT  ==============
# by using OS module which have path sub Module which has isFile() method to check
#       eg: os.path.isFile(filename)








