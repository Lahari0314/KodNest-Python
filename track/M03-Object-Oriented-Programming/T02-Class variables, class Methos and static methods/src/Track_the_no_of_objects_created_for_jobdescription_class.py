class JobDescription:
    count=0
    def __init__(self,role,company):
        self.role=role
        self.company=company
        JobDescription.count+=1

j1=JobDescription("Python","KodNest")
j2=JobDescription("Java","KodNest")
j3=JobDescription("C++","KodNest")

print("Jobs created:",JobDescription.count)