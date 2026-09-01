class TrainingBatch:
    batch="Python batch 1"
    def __init__(self,name):
        self.name=name

s1=TrainingBatch("raj")
s2=TrainingBatch("manas")

print(TrainingBatch.batch)
print(s1.batch)
print(s2.batch)

s1.batch="Java Batch 1"

print(s1.batch)
print(s2.batch)