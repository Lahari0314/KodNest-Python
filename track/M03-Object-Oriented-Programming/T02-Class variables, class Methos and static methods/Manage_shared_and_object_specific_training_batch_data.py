class TrainingBatch:
    platform="KodNest"
    batch="Python Batch 1"
    def __init__(self,name,score):
        self.name=name
        self.score=score

n1=input()
s1=int(input())

n2=input()
s2=int(input())

b1=TrainingBatch(n1,s1)
b2=TrainingBatch(n2,s2)

print("Platform:",TrainingBatch.platform)
print("Batch:",TrainingBatch.batch)
print("Name:",b1.name)
print("Score:",b1.score)
print("Name:",b2.name)
print("Score:",b2.score)
