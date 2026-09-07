class SkillAnalyzer:
    def __init__(self,skills,required):
        self.skills=set(skills)
        self.required=set(required)

    def get_matched(self):
        return self.skills&self.required

class MatchScoreCalculator(SkillAnalyzer):
    def get_score(self):
        matched=len(self.get_matched())
        total=len(self.required)
        return (matched/total)*100

class MissingSkillDetector(SkillAnalyzer):
    def get_missing(self):
        return sorted(self.required-self.get_matched())

skills=input().split()
required=input().split()
miss=MissingSkillDetector(skills,required)
print("Missing Skills:",", ".join(miss.get_missing()) if miss.get_missing() else None)
cal=MatchScoreCalculator(skills,required)
print(f"Matched skills: {cal.get_score():.2f}")