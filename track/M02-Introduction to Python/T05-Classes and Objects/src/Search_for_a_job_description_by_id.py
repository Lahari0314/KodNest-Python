class JobDescriptions:
    def __init__(self,id,company,role):
        self.id=id
        self.company=company
        self.role=role

    def __str__(self):
        return f"{self.id}-{self.company}-{self.role}"

class PlacementManager:
    def __init__(self):
        self.job_descriptions=[]

    def add_jobs(self,job):
        self.job_descriptions.append(job)

    def search_by_id(self,id):
        if not self.job_descriptions:
            return None
        for job in self.job_descriptions:
            if job.id==id:
                return job
        return None

manager=PlacementManager()
n=int(input())
for i in range(n):
    id=int(input())
    company=input()
    role=input()
    job=JobDescriptions(id,company,role)
    manager.add_jobs(job)

search_id=int(input())
result=manager.search_by_id(search_id)
if result:
    print(result)
else:
    print("No job description found with the given ID")