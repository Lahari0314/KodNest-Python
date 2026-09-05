class StudentProfile:
    def __init__(self,name):
        self.name=name

    def display(self):
        return f"Student: {self.name}"

class Fresher(StudentProfile):
    pass

class Experienced(StudentProfile):
    pass

n1=input()
n2=input()
f=Fresher(n1)
e=Experienced(n2)
print("Fresher",f.display())
print("Experienced",e.display())