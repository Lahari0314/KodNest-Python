n=int(input())
registrations=set()
for i in range(n):
    registrations.add(input())
search=input()
unique=len(registrations)
duplicates=n-len(registrations)
print("Unique elements:",unique)
print("Duplicate elements:",duplicates)
if search in registrations:
    print("Found")
else:
    print("Not Found")
