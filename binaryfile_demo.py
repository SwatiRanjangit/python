import pickle
from pickle import *
#==================== PICKLING UNPICKLING =============================
# used for binary file
#pickling : process of write object data into file , use : pickle.dump()
# unpickling: process of read object data from file,  use: pickle.load()

class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def display(self):
        print("id is: ",self.id)
        print("name is: ", self.name)
        print("salary is: ", self.sal)
#
# e = Employee(23,"swati",560000)
# e.display()

#=========== PICKLING OF DATA ====

# with open("emp_details.dat","wb") as f:
#     e = Employee(23, "swati", 560000)
#     pickle.dump(e,f)
#     print("data is dumbed into bonary file ")

#=========== UNPICKLING OF DATA ====
with open("emp_details.dat","rb") as f:
    obj = pickle.load(f)
    print("Data after unpickling: ")
    obj.display()







