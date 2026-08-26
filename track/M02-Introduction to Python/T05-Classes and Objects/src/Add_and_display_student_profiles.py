class StudentProfile:
    def __init__(self,name,id,course):
        self.name=name
        self.id=id
        self.course=course
    def __str__(self):
        return f"{self.id}-{self.name}-{self.course}"

class PlacementManager:
    def __init__(self):
        self.student_profiles=[]
    
    def add_profile(self,student_profile):
        self.student_profiles.append(student_profile)

    def display(self):
        if not self.student_profiles:
            print("No profiles found")
        else:
            print("STUDENT PROFILES")
            for profile in self.student_profiles:
                print(profile)

manager=PlacementManager()
n=int(input())
for i in range(n):
    name=input()
    id=int(input())
    course=input()
    student=StudentProfile(name,id,course)
    manager.add_profile(student)

manager.display()

    