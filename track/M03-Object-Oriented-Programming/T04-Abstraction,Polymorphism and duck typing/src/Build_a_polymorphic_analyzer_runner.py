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
    def analyze(self):
        matched=len(self.get_matched())
        total=len(self.required)
        x=(matched/total)*100
        if x:
            return x
        else:
            return 0.00

class MissingSkillDetector(SkillAnalyzer):
    def analyze(self):
        skill=sorted(self.required-self.get_matched())
        if skill:
            return skill

skills=input().split()
required=input().split()
miss=MissingSkillDetector(skills,required)
print("Missing Skills:",", ".join(miss.analyze()) if miss.analyze() else None)
cal=MatchScoreCalculator(skills,required)
print(f"Matched skills: {cal.analyze():.2f}")