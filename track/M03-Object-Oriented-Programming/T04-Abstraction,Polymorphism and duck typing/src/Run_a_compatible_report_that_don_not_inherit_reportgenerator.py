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

class SimpleTextReport:
    def __init__(self,message):
        self.message=message
    def generate(self):
        return f"Generating simple text report: {self.message}"

def run(reports):
    for i in reports:
        print(i.generate())

text=input()
reports=[StudentReport(),PlacementReport(),SimpleTextReport(text)]
run(reports)