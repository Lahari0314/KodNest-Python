class JobDescription:
    def __init__(self,job_id,title,company,location="Remote",is_active=False):
        self.job_id=job_id
        self.title=title
        self.company=company
        self.location=location
        self.is_active=is_active
    def __str__(self):
        status="Active" if self.is_active else "Closed"
        return f"Job ID:{self.job_id}\nTitle:{self.title}\nCompany:{self.company}\nLocation:{self.location}\nStatus:{status}"
job1=JobDescription(101,"Software Engineer","Google","New York",True)
job2=JobDescription(102,"Data Scientist","Microsoft","San Francisco",True)
job3=JobDescription(103,"Project Manager","Amazon","Seattle",False)
jobs=[job1,job2,job3]
for job in jobs:
    print(job)