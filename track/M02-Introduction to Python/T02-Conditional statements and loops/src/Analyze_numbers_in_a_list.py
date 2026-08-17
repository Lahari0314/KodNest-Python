n=int(input())
target=int(input())
count=0
total=0
found=False
for i in range(n):
    if i%3==0:
        total+=i
        count+=1
        if i==target:
            found=True
print(total)
print(count)
print("Target Found:Yes" if found else "Target Found:No")