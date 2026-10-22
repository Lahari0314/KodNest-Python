def change(names):
    return [name.upper() for name in names]

names=input().split()
print(*change(names))