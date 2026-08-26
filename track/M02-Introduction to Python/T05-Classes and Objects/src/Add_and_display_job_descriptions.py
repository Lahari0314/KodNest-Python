class JobDescription:
    def __init__(self,id,company,role):
        self.id=id
        self.company=company
        self.role=role
    
    def __str__(self):
        return f"{self.id}-{self.company}-{self.role}"

class PlacementManager:
    def __init__(self):
        self.job_descriptions=[]

    def add_job(self,job):
        self.job_descriptions.append(job)

    def display(self):
        if not self.job_descriptions:
            print("No job descriptions available")
        else:
            print("JOB DESCRIPTIONS")
            for job in self.job_descriptions:
                print(job)


manager=PlacementManager()
n=int(input())
for i in range(n):
    id=int(input())
    company=input()
    role=input()

    job=JobDescription(id,company,role)
    manager.add_job(job)

manager.display()