class CSVExporter:
    def __init__(self,file):
        self.file=file
    def export(self):
        return f"CSV Export: {self.file}.csv"

class JSONExporter:
    def __init__(self,file):
        self.file=file
    def export(self):
        return f"JSON Export: {self.file}.json"

class PDFExporter:
    def __init__(self,file):
        self.file=file
    def export(self):
        return f"PDF Export: {self.file}.pdf"

def run(exports):
    for i in exports:
        print(i.export())

name=input()
exports=[CSVExporter(name),JSONExporter(name),PDFExporter(name)]
run(exports)