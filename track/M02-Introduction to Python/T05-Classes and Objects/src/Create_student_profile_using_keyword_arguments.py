class StudentProfile:
    def __init__(self,name,id,course,score=0.0,is_placed=False):
        self.name=name
        self.id=id
        self.course=course
        self.score=score
        self.is_placed=is_placed
    def __str__(self):
        placement_status= "Placed" if self.is_placed else "Not Placed"
        return f"Name:{self.name}\nID:{self.id}\nCourse:{self.course}\nScore:{self.score}\nIs Placed:{placement_status}"
student1 = StudentProfile("Asha",102,"Python",85.5,True)
print(student1)
student2=StudentProfile("Raju",101,"Java",78.5,False)
print(student2)