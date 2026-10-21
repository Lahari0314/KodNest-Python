def calculate(prices,discount):
    return [price-(price*discount/100) for price in prices]

prices=list(map(int,input().split()))
discount=int(input())
print(*calculate(prices,discount))