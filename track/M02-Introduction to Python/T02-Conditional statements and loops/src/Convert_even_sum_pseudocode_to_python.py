n=int(input())
num=1
total=0
while num<=n:
    if num%2==0:
        total+=num
    num+=1
print(total)