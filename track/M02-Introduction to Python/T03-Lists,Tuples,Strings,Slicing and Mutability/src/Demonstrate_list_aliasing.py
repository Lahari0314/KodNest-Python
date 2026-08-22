original=[]
for i in range(3):
    original.append(int(input()))
alias = original
replace = int(input())
additional=int(input())
alias[0]=replace
original.append(additional)
print(original)
print(alias)
print(original is alias)
