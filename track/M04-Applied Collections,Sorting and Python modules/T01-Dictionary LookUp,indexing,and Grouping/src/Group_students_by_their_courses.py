def group(students):
    students_by_course={}
    for name,course in students:
        if course not in students_by_course:
            students_by_course[course]=[]
        students_by_course[course].append(name)

    return students_by_course

n=int(input())
students=[]
for i in range(n):
    name,course=input().split()
    students.append((name,course))

result=group(students)
for course,names in result.items():
    print(course+": "+" ".join(names))