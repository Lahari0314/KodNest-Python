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

    def analyze(self):
        pass

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        student_skills=self.student.skills
        required_skills=self.job.required
        missing=[]
        for skill in required_skills:
            if skill not in student_skills:
                missing.append(skill)

        return missing


student_skills=input().split(",")
required_skills=input().split(",")
student=StudentProfile(student_skills)
job=JobDescription(required_skills)
result=MissingSkillDetector(student,job)
print(result.analyze())