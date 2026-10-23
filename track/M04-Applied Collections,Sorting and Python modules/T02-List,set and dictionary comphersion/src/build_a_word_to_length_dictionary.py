def w2l(words):
    return {word:len(word) for word in words}

words=input().split()
result=w2l(words)
for k,v in result.items():
    print(k+"-"+str(v))