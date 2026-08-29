class StudentProfile:
    def __init__(self,student_id,name,score,skills):
        self.__id=student_id
        self.__name=name
        self.__score=score
        self.__skills=skills

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @property
    def skills(self):
        return tuple(self.__skills)

    @name.setter
    def name(self,new_name):
        cleaned=new_name.strip()
        if cleaned:
            self.__name=cleaned

    @score.setter
    def score(self,new_score):
        if 0<=new_score<=100:
            self.__score=new_score

    def add_skill(self,skill):
        cleaned=skill.strip()
        if cleaned and cleaned not in self.__skills:
            self.__skills.append(cleaned)

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nScore: {self.score}\nSkills: {", ".join(self.skills)}"

id=int(input())
name=input()
score=int(input())
skills=input()

skills=skills.split(",")

student=StudentProfile(id,name,score,skills)
new_score=int(input())
student.score=new_score

new_skill=input()
student.add_skill(new_skill)

print(student)
