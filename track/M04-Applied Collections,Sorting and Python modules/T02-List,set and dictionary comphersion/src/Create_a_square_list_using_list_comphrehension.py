def square(numbers):
    return [i*i for i in numbers]

numbers=list(map(int,input().split()))
print(*square(numbers))