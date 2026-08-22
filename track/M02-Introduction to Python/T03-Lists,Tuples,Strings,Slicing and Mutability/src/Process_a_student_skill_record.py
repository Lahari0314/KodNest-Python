skills=[]
for i in range(5):
    skills.append(input())
skill_record=tuple(skills)
print("Skills Record:",skill_record)
print("First Three:",skill_record[:3])
print("Last Two:",skill_record[-2:])
print("Alternative skills:",skill_record[::2])
print("Reverse skills:",skill_record[::-1])