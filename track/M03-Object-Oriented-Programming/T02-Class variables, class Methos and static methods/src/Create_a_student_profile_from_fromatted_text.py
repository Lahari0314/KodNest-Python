class StudentProfile:
    def __init__(self,id,name,course,exp):
        self.id=id
        self.name=name
        self.course=course
        self.exp=exp

    @classmethod
    def from_string(cls,student_string):
        id,name,course,exp=student_string.split("|")
        return cls(id,name,course,exp)

data=input().strip()
s=StudentProfile.from_string(data)
print("Student ID:",s.id)
print("Student Name:",s.name)
print("Student Course:",s.course)
print("Student Experience:",s.exp)

    