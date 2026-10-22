def extract(numbers):
    return [i for i in numbers if i>0]

numbers=list(map(int,input().split()))
print(*extract(numbers))