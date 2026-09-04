class JobDescription:
    platform="Kodnest Jobs"
    def __init__(self,role,company,exp):
        self.role=role
        self.company=company
        self.exp=exp

    @staticmethod
    def is_valid(exp):
        return 0<=exp<=20

    @classmethod
    def from_text(cls,text):
        role,company,exp=text.split("|")
        if JobDescription.is_valid(int(exp)):
            return cls(role.strip().title(),company.strip(),int(exp))
        else:
            return None

    def __str__(self):
        return f"Platform: {JobDescription.platform}\nRole: {self.role}\nCompany: {self.company}\nExperience: {self.exp} years"

job1=JobDescription.from_text("   python developer | kodnest   | 2   ")
if job1:
    print(job1)
else:
    print("Invalid Experience")