students=int(input())
total=0
passed=0
failed=0
for i in range(students):
    marks=int(input())
    total+=marks
    if marks>=40:
        passed+=1
    else:
        failed+=1
print(total)
print(passed)
print(failed)
if failed==0:
    print("Total batch passed")
else:
    print("Batch needs improvement")