from abc import ABC,abstractmethod
class SkillAnalyzer(ABC):
    def __init__(self,skills,required):
        self.skills=set(skills)
        self.required=set(required)

    def get_matched(self):
        return self.skills&self.required
    @abstractmethod
    def analyze(self):
        pass

class MatchScoreCalculator(SkillAnalyzer):
    def get_score(self):
        matched=len(self.get_matched())
        total=len(self.required)
        return (matched/total)*100

    def analyze(self):
        x=self.get_score()
        if x:
            return f"Matched Score: {x:.2f}%"
        else:
            return f"Matched Score: 0.00%"

class MissingSkillDetector(SkillAnalyzer):
    def get_missing(self):
        return sorted(self.required-self.get_matched())
    def analyze(self):
        skill=self.get_missing()
        if skill:
            return f"Missing Skills: {", ".join(skill)}"
        return "Missing Skills: None"

class RequiredSkillCounter:
    def __init__(self,required_skills):
        self.skills=required_skills
    def analyze(self):
        return f"Required Skill Count: {len(self.skills)}"

def run_analyzers(analyzers):
    for i in analyzers:
        print(i.analyze())

student_skills=input().split()
required_skills=input().split()
analyzers=[MatchScoreCalculator(student_skills,required_skills),MissingSkillDetector(student_skills,required_skills),RequiredSkillCounter(required_skills)]
run_analyzers(analyzers)