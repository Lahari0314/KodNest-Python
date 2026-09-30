def build_employee_index(employees):
    employee_by_id={}
    for employee in employees:
        id=employee["employee_id"]
        employee_by_id[id]=employee
    return employee_by_id

n=int(input())
employees=[]
for i in range(n):
    employee_id,name,department=input().split()
    employees.append({
        "employee_id":employee_id,
        "name":name,
        "department":department
    })
required=input()
employee=build_employee_index(employees)
result=employee.get(required)
if result is not None:
    print(result["name"])
    print(result["department"])
else:
    print("Employee not found")