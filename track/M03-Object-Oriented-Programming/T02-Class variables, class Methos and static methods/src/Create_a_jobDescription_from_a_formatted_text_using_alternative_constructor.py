class JobDescription:
    def __init__(self,role,company,exp,skills):
        self.role=role
        self.company=company
        self.exp=exp
        self.skills=skills

    def __str__(self):
        return f"Job: {self.role}\nCompany: {self.company}\nExperience: {self.exp}\nSkills: {', '.join(self.skills)}"

    @classmethod
    def from_formatted_text(cls,text):
        role,company,exp,skills=text.split(";")
        return cls(role.strip(),company.strip(),int(exp),[skill.strip() for skill in skills.split(",")])

text="Python Developer;KodNest   ;2;Python,  Java,  C++"
j1=JobDescription.from_formatted_text(text)
print(j1)