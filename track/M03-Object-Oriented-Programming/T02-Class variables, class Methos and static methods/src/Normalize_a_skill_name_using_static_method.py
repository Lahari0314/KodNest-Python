class StudentProfile:
    @staticmethod
    def normalize(skill):
        skill=skill.strip().lower().split()
        return "_".join(skill)

skill=input()
res=StudentProfile.normalize(skill)
print("Normalized skill:",res)