from abc import ABC,abstractmethod
class Notification(ABC):
    @abstractmethod
    def notify(self):
        pass

class EmailNotification(Notification):
    def __init__(self,message):
        self.message=message
    def send(self):
        return f"Email: {self.message}"

    def notify(self):
        print(self.send())

class SMSNotification(Notification):
    def __init__(self,message):
        self.message=message
    def send(self):
        return f"SMS: {self.message}"
    def notify(self):
        print(self.send())

message=input()
notifications=[EmailNotification(message),SMSNotification(message)]
for i in notifications:
    i.notify()