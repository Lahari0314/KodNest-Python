class StudentProfile:
    def __init__(self,id,name,course,experience,skills):
        self.id=id
        self.name=name
        self.course=course
        self.experience=experience
        self.skills=skills


id=int(input())
name=input().strip()
course=input().strip()
experience=int(input())
skills=input().split()
s=StudentProfile(id,name,course,experience,skills)

print("Student ID:",s.id)
print("Name:",s.name)
print("Course:",s.course)
print("Experience:",s.experience)
print("Skills:"," ".join(s.skills))