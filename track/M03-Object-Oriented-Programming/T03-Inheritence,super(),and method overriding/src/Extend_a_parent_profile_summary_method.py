class Profile:
    def __init__(self,name):
        self.name=name

    def summary(self):
        return f"Name: {self.name}"

class StudentProfile(Profile):
    def __init__(self,name,course):
        super().__init__(name)
        self.course=course

    def summary(self):
        print(super().summary())
        print("Course:",self.course)


name=input()
course=input()
s=StudentProfile(name,course)
s.summary()