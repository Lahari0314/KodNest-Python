class StudentProfile:
    def __init__(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course

id1=int(input())
n1=input().strip()
c1=input().strip()

id2=int(input())
n2=input().strip()
c2=input().strip()

student1=StudentProfile(id1,n1,c1)
student2=StudentProfile(id2,n2,c2)

print(student1.id,student1.name,student1.course)
print(student2.id,student2.name,student2.course)
