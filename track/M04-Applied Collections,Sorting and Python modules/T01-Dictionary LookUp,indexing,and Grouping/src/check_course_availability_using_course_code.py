def check(courses,code):
    if code in courses:
        if courses[code]>0:
            return f"Seats available:{courses[code]}"
        else:
            return "Seats full"
    else:
        return "Course not found"

course={
    "Py101":20,
    "Sql02":0,
    "JV103":7,
    "AI104":3
}
required=input()
print(check(course,required))