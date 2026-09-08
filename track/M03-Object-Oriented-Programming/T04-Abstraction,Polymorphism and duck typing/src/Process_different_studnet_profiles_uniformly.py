class StudentProfile:
    def show_profile(self):
        pass

class Fresher(StudentProfile):
    def __init__(self,name,graduation):
        self.name=name
        self.year=graduation

    def show_profile(self):
        return f"{self.name} - Graduating - {self.year}"

class Experienced(StudentProfile):
    def __init__(self,name,experience):
        self.name=name
        self.exp=experience
    def show_profile(self):
        return f"{self.name} - Experience - {self.exp} years"

fn=input()
fg=int(input())
en=input()
eg=int(input())
ls=[Fresher(fn,fg),Experienced(en,eg)]
for i in ls:
    print(i.show_profile())
