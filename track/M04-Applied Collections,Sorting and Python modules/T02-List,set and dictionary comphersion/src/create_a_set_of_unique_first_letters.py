def unique(words):
    return {word[0] for word in words}

words=input().split()
result=unique(words)
ordered_list=[i for i in "abcdefghijklmnopqrstuvwxyz" if i in result]
print(*ordered_list)