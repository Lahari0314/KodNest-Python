def calculator(n1,n2,op):
    if op=="+":
        return n1+n2
    elif op=="-":
        return n1-n2
    elif op=="*":
        return n1*n2
    elif op=="/":
        return n1/n2

n1=int(input())
n2=int(input())
operator=input()
result=calculator(n1,n2,operator)
print(result)