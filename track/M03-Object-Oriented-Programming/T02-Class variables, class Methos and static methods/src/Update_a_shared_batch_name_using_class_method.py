class TrainingBatch:
    batch="Python batch 1"
    def __init__(self,name):
        self.name=name

    @classmethod
    def update_batch(cls,new_batch):
        cls.batch=new_batch

    def display(self):
        print(self.name,self.batch)

s1=TrainingBatch("raj")
s2=TrainingBatch("manas")

s1.display()
s2.display()

TrainingBatch.update_batch("Java Batch 1")

s1.display()
s2.display()