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

amount=int(input())
u=UPIPayment(amount)
u.process_payment()