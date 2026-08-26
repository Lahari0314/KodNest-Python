class StudentProfiles:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course

    def __str__(self):
        return f"{self.id}-{self.name}-{self.course}"

class PlacementManager:
    def __init__(self):
        self.students=[]

    def add_students(self,student):
        self.students.append(student)

    def filter_by_course(self,course):
        return [s for s in self.students if s.course==course]

manager=PlacementManager()
n=int(input())
for i in range(n):
    id=int(input())
    name=input().strip()
    course=input().strip()
    student=StudentProfiles(id,name,course)
    manager.add_students(student)

course=input().strip().title()
result=manager.filter_by_course(course)
for s in result:
    print(s)