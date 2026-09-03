class StudentProfile:
    def __init__(self,name,experience):
        self.name=name
        self.experience=experience

    @staticmethod
    def is_valid_experience(experience):
        return 0<=experience<=40

    def display(self):
        print("Profile Created")
        print("Name:",self.name)
        print("Experience:",self.experience)

name=input()
exp=int(input())
res=StudentProfile.is_valid_experience(exp)
if res:
    s=StudentProfile(name,exp)
    s.display()
else:
    print("Invalid experience")

    