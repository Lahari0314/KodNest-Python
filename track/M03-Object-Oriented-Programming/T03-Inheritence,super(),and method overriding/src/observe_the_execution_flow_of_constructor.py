class Employee:
    def __init__(self,name):
        print("Employee constructor")
        self.name=name

class Developer(Employee):
    def __init__(self,name):
        print("Developer constructor started")
        super().__init__(name)
        print("Developer constructor ended")


name=input()
d=Developer(name)
print("Developer:",d.name)