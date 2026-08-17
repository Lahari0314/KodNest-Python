n=int(input())
pos=0
neg=0
zero=0
total=0
for i in range(n):
    num=int(input())
    if num>0:
        pos+=1
    elif num<0:
        neg+=1
    else:
        zero+=1
    total+=num
print(pos)
print(neg)
print(zero)
print(total)