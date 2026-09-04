from os import stat
class Student:
    @staticmethod
    def is_valid(skill):
        return skill.lower().replace(" ","").isalpha()

    @staticmethod
    def normalize(skill):
        skill=skill.strip().lower().split()
        return "_".join(skill)

skill=input()
if Student.is_valid(skill):
    print("Valid Skill")
    print("Normalized Skill:",Student.normalize(skill))
else:
    print("Invalid skill") 