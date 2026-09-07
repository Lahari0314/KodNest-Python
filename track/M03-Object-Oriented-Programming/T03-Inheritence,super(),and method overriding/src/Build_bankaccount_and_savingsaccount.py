class BankAccount:
    def __init__(self,holder):
        self.holder=holder

    def get_holder(self):
        return f"Account Holder: {self.holder}"

class SavingsAccount(BankAccount):
    def __init__(self,holder,balance):
        super().__init__(holder)
        self.balance=balance

    def get_balance(self):
        return f"Balance: {self.balance}"

name=input()
balance=int(input())
s=SavingsAccount(name,balance)
print(s.get_holder())
print(s.get_balance())