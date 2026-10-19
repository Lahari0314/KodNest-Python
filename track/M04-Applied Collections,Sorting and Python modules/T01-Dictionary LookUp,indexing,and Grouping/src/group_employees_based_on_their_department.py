def group(employees):
    employees_by_department={}
    for name,depart in employees:
        if depart not in employees_by_department:
            employees_by_department[depart]=[]
        employees_by_department[depart].append(name)

    return employees_by_department

n=int(input())
employees=[]
for i in range(n):
    name,depart=input().split()
    employees.append((name,depart))

result=group(employees)
for depart,names in result.items():
    print(depart+": "+" ".join(names))