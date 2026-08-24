n=int(input())
dict={}
for i in range(n):
    word=input().strip().lower()
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
for key,value in dict.items():
    print(key,value)