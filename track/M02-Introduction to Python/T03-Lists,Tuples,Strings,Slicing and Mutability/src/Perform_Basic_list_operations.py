n=int(input())
scores=[]
for i in range(n):
    scores.append(int(input()))
search=int(input())
print("highest score:",max(scores))
print("lowest scores:",min(scores))
print("total scores:",sum(scores))
if search in scores:
    print("found")
else:
    print("not found")