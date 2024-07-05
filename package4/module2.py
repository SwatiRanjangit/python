class Student:
    def __init__(self,id,name,add):
        self.id=id
        self.name = name
        self.add = add



    def displayStu(self):
        print("student id is: ", self.id)
        print("student name is: ", self.name)
        print("student address is: ", self.add)