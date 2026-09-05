class Course:
    def __init__(self,course):
        self.course=course

    def display(self):
        print("Course:",course)

class CodingCourse(Course):
    pass

course=input()
c=CodingCourse(course)
c.display()