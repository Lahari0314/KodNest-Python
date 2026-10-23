def lengths(words):
    return {len(word) for word in words}

words=input().split()
unique=lengths(words)
ordered_list=[length for length in range(1,21) if length in unique]
print(*ordered_list)