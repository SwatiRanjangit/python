class Employee:
    def __init__(self,id,name,add):
        self.id=id
        self.name = name
        self.add = add



    def displayEmp(self):
        print("emp id is: ", self.id)
        print("emp name is: ", self.name)
        print("emp address is: ", self.add)

