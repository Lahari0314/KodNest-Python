class StudentProfile:
    def __init__(self,id,name,course,experience,skills):
        self.id=id
        self.name=name
        self.course=course
        self.experience=experience
        self.skills=skills

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nCourse: {self.course}\nExperience: {self.experience}\nSkills: {', '.join(self.skills)}"

id=int(input())
name=input().strip()
course=input().strip()
experience=int(input())
skills=input().split()

s=StudentProfile(id,name,course,experience,skills)
print(s)