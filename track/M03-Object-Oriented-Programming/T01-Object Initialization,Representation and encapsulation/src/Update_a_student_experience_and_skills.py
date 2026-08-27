class StudentProfile:
    def __init__(self,name,experience,skills):
        self.name=name
        self.experience=experience
        self.skills=skills

    def update_experience(self,new_experience):
        self.experience=new_experience

    def add_skills(self,new_skills):
        self.skills.extend(new_skills)


name=input().strip()
experience=int(input())
skills=input().split()

s=StudentProfile(name,experience,skills)

new_experience=int(input())
s.update_experience(new_experience)

new_skills=input().split()
s.add_skills(new_skills)
print("Name:",s.name)
print("Experience:",s.experience)
print("Skills:",",".join(s.skills))
