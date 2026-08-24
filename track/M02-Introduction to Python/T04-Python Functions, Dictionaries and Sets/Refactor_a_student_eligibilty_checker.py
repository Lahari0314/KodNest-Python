def checker(marks,attendance,project_completed):
    if marks>=60 and attendance>=75 and project_completed=="yes":
        return "Eligible"
    else:
        return "Not Eligible"

result=checker(65,80,"yes")
print(result)