def missings(student_skills,required_skills):
    student=[skill.lower().strip() for skill in student_skills]
    miss=[]
    for skill in required_skills:
        if skill.lower().strip() not in student:
            miss.append(skill.strip())
    return miss

n=int(input())
student_skills=input().split(",") if n>0 else []
m=int(input())
required_skills=input().split(",") if m>0 else []
result=missings(student_skills,required_skills)
if result:
    print(", ".join(result))
else:
    print("No Missing Skills")