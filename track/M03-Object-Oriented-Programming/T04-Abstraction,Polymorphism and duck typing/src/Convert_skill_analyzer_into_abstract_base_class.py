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
            return x
        else:
            return 0.00

class MissingSkillDetector(SkillAnalyzer):
    def get_missing(self):
        return sorted(self.required-self.get_matched())
    def analyze(self):
        skill=self.get_missing()
        if skill:
            return skill

skills=input().split()
required=input().split()
miss=MissingSkillDetector(skills,required)
print("Missing Skills:",", ".join(miss.analyze()) if miss.analyze() else None)
cal=MatchScoreCalculator(skills,required)
print(f"Matched skills: {cal.analyze():.2f}")