class CandidateProfile:
    def __init__(self,name,email,score):
        self.name=name
        self._email=email
        self.__score=score

    def get_score(self):
        return self.__score

    def get_email(self):
        return self._email
name=input()
email=input()
score=int(input())

candidate=CandidateProfile(name,email,score)
print("CANDIDATE PROFILE")
print("Name:",candidate.name)
print("Email:",candidate.get_email())
print("Score:",candidate.get_score())
