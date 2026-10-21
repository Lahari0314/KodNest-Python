def check(students,cutoff):
    return [s for s in students if s[1]>cutoff]

students=[['Asha',90],['Meera',85],['Raju',50],['Rahul',65]]
cutoff=int(input())
result=check(students,cutoff)
for _ in result:
    print(_[0])