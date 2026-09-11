class Employee:
    def show_detail(self):
        pass

class Permanent(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show_detail(self):
        return f"{self.name} - Permanent - Salary: {self.salary}"

class Contract(Employee):
    def __init__(self,name,months):
        self.name=name
        self.months=months

    def show_detail(self):
        return f"{self.name} - Contract - Months:{self.months}"

n1=input()
salary=int(input())
n2=input()
m=int(input())
e=[Permanent(n1,salary),Contract(n2,m)]
for i in e:
    print(i.show_detail())