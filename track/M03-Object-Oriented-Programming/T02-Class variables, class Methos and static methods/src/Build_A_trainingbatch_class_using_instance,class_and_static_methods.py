class Training:
    batch="Kodnest python 1"
    count=0
    def __init__(self,name,att):
        self.name=name
        self.att=att
        Training.count+=1

    def display(self):
        return f"{self.name}: {self.att}%"

    @classmethod
    def change_batch(cls,new_batch):
        cls.batch=new_batch

    @staticmethod
    def is_valid(att):
        return att>=0 and att<=100

n=int(input())
students=[]
for i in range(n):
    name=input()
    att=int(input())
    if Training.is_valid(att):
        students.append(Training(name,att))
print("Batch:",Training.batch)
print("Valid students:",Training.count)
for i in students:
    print(i.display())