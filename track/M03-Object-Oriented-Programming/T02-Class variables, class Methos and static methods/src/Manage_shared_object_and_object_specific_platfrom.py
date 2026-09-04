class Course:
    platform="KodNest Learning"
    count=0
    def __init__(self,course,days,fee):
        self.course=course
        self.days=days
        self.fee=fee
        Course.count+=1

    def show_course(self):
        print(f"Course {Course.count}: {self.course}")
        print(f"Days: {self.days}")
        print(f"Fee: {self.fee}")
print("Platform:",Course.platform)
c1=Course("Python",30,10000)
c1.show_course()
c2=Course("Java",40,20000)
c2.show_course()
c3=Course("C++",50,30000)
c3.show_course()
