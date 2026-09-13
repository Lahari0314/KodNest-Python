from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass

class EmailNotification(Notification):
    def __init__(self,message):
        self.message=message
    def notify(self):
        return f"Email: {self.message}"


class SMSNotification(Notification):
    def __init__(self,message):
        self.message=message
    def notify(self):
         return f"SMS: {self.message}"

message=input()
notifications=[EmailNotification(message),SMSNotification(message)]
for i in notifications:
    print(i.notify())