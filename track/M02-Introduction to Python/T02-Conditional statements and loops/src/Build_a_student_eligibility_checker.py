marks=int(input())
attendance = int(input())
completion=input()
if marks>=60 and attendance>=75 and completion=="yes":
    print("Eligible")
else:
    print("Not Eligible")