class StudentProfile:
    def __init__(self,student_skills):
        self.skills=[skill.lower().strip() for skill in student_skills]

class JobDescription:
    def __init__(self,required_skills):
        self.required=[skill.lower().strip() for skill in required_skills]

class SkillAnalyzer:
    def __init__(self,student,job):
        self.student=student
        self.job=job

class MatchScoreCalculator(SkillAnalyzer):
    def analyze(self):
        match=set(self.student.skills)&set(self.job.required)
        required=self.job.required
        if len(required)==0:
            return 0
        per=(len(match)/len(required))*100
        return per

student_skills=input().split(",")
required_skills=input().split(",")
student=StudentProfile(student_skills)
job=JobDescription(required_skills)
score=MatchScoreCalculator(student,job)
print(score.analyze())