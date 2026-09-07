class SkillAnalyzer:
    def __init__(self,skills,required):
        self.skills=set(skills)
        self.required=set(required)

    def get_matched(self):
        return sorted(self.skills&self.required)


skills=input().split()
required=input().split()
analyzer=SkillAnalyzer(skills,required)
print("Matched skills:",", ".join(analyzer.get_matched()) if analyzer.get_matched() else None)