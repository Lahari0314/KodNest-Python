def percentage(required,matched):
    if required==0:
        return 0
    return (matched/required)*100

required=int(input())
matched=int(input())
print(percentage(required,matched))