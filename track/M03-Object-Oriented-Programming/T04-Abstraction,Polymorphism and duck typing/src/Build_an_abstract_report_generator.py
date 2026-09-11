from abc import ABC,abstractmethod
class ReportGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class StudentReport(ReportGenerator):
    def __init__(self,name):
        self.name=name

    def generate(self):
        print("Generating report for student ",self.name)

name=input()
s=StudentReport(name)
s.generate()