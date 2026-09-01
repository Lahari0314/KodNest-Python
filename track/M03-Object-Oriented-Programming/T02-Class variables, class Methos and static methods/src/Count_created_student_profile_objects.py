class StudentProfile:
    count=0
    def __init__(self,name):
        self.name=name
        StudentProfile.count+=1

n=int(input())
for i in range(n):
    s=input()
    sob=StudentProfile(s)

print("Objects Created:",StudentProfile.count)