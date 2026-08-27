class JobDescription:
    def __init__(self,id,company,role,experience,skills,is_active):
        self.id=id
        self.company=company
        self.role=role
        self.experience=experience
        self.skills=skills
        self.is_active=is_active

    def __str__(self):
        self.is_active="Active" if self.is_active=="yes" else "Closed"
        return f"ID: {self.id}\nCompany: {self.company}\nRole: {self.role}\nExperience: {self.experience}\nSkills: {', '.join(self.skills)}\nIs Active: {self.is_active}"

id=int(input())
company=input().strip()
role=input().strip()
experience=int(input())
skills=input().split()
is_active=input().strip()

j=JobDescription(id,company,role,experience,skills,is_active)
print(j)