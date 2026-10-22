def convert(temperatures):
    return [(celsius*9/5)+32 for celsius in temperatures]

temperatures=list(map(int,input().split()))
print(*convert(temperatures))