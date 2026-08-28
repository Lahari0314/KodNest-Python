class StudentProfile:
    def __init__(self,name,score):
        self.name=name
        self.__score=score

    def get_score(self):
        return self.__score

    def update_score(self,new_score):
        if 0<=new_score<=100:
            self.__score=new_score
        else:
            print("Invalid score")

name=input()
score=int(input())

student=StudentProfile(name,score)

new_score=int(input())
student.update_score(new_score)
print("Name:",student.name)
print("Score:",student.get_score())
