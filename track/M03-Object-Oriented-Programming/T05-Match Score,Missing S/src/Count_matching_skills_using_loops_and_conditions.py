def count_skills(student_skills,required_skills):
    count=0
    for skill in required_skills:
        if skill in student_skills:
            count+=1
    return count

student_skills=input().split()
required=input().split()
print(count_skills(student_skills,required))