class StudentProfile:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course
    
    def __str__(self):
        return f"{self.id}-{self.name}-{self.course}"

class StudentManager:
    def __init__(self):
        self.student_profiles=[]

    def add_student(self,student):
        self.student_profiles.append(student)

    def search_by_id(self,id):
        for student in self.student_profiles:
            if student.id==id:
                return student
        return None



manager=StudentManager()
n=int(input())
for i in range(n):
    id=int(input())
    name=input()
    course=input()

    student=StudentProfile(id,name,course)
    manager.add_student(student)

require_id=int(input())
result=manager.search_by_id(require_id)
if result:
    print(result)
else:
    print("Student not found")