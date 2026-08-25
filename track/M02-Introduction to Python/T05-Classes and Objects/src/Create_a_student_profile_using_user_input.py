class StudentProfile:
    def __init__(self,name,id,course,score,is_placed):
        self.name=name
        self.id=id
        self.course=course
        self.score=score
        self.is_placed=is_placed
    def __str__(self):
        placement_status= "Placed" if self.is_placed else "Not Placed"
        return f"Name:{self.name}\nID:{self.id}\nCourse:{self.course}\nScore:{self.score}\nIs Placed:{placement_status}"
name=input()
id=int(input())
course=input()
score=float(input())
placed=input().strip().lower()
is_placed=True if placed=="yes" else False
student = StudentProfile(name,id,course,score,is_placed)
print(student)