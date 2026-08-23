def sign_checker(n):
    if n>0:
        return "Positive"
    elif n<0:
        return "Negative"
    else:
        return "Zero"

n=int(input())
result=sign_checker(n)
print(result)