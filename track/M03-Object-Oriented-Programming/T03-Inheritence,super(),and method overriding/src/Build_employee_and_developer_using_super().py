class Employee:
    def __init__(self,name):
        self.name=name

class Developer(Employee):
    def __init__(self,name,language):
        super().__init__(name)
        self.lan=language

    def display(self):
        print("Name:",name)
        print("Language:",self.lan)


name=input()
lan=input()
d=Developer(name,lan)
d.display()