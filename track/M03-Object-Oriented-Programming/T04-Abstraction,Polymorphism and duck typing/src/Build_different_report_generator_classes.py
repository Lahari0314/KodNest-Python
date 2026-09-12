from abc import ABC,abstractmethod
class ReportGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class StudentReport(ReportGenerator):
    def generate(self):
        return "Generating student report"

class PlacementReport(ReportGenerator):
    def generate(self):
        return "Generating placement report"

class AttendanceReport(ReportGenerator):
    def generate(self):
        return "Generating attendance report"

n=int(input())
reports=[]
for i in range(n):
    x=input()
    if x=="STUDENT":
        reports.append(StudentReport())
    elif x=="PLACEMENT":
        reports.append(PlacementReport())
    else:
        reports.append(AttendanceReport())

for i in reports:
    print(i.generate())