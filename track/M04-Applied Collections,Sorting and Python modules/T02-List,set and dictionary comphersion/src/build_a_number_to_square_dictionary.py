def square(numbers):
    return {i:i*i for i in numbers}

numbers=list(map(int,input().split()))
result=square(numbers)
for k,v in result.items():
    print(str(k)+" "+str(v))