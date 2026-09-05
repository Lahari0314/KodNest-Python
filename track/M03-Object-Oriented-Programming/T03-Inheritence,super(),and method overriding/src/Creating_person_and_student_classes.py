class Person:
    def display(self,name):
        print("Student Name:",name)

class Student(Person):
    pass

name=input()
s=Student()
s.display(name)