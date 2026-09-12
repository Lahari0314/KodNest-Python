from abc import ABC,abstractmethod
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self):
        pass


class UPIPayment(PaymentProcessor):
    def __init__(self,amount):
        self.amount=amount

    def process_payment(self):
        print("Processing UPI payment of",self.amount)

class CardPayment(PaymentProcessor):
    def __init__(self,amount):
        self.amount=amount

    def process_payment(self):
        print("Processing card payment of",self.amount)

class NetBankingPayment(PaymentProcessor):
    def __init__(self,amount):
        self.amount=amount

    def process_payment(self):
        print("Processing net banking payment of",self.amount)

upi=int(input())
card=int(input())
net=int(input())
payments=[UPIPayment(upi),CardPayment(card),NetBankingPayment(net)]
for i in payments:
    i.process_payment()