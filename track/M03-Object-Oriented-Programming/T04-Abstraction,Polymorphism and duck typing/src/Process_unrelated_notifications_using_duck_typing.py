class EmailNotification():
    def __init__(self,message):
        self.message=message
    def notify(self):
        return f"Email: {self.message}"


class SMSNotification():
    def __init__(self,message):
        self.message=message
    def notify(self):
         return f"SMS: {self.message}"

class PushNotification():
    def __init__(self,message):
        self.message=message
    def notify(self):
         return f"Push: {self.message}"

def run_notification(notifications):
    for i in notifications:
        print(i.notify())

message=input()
notifications=[EmailNotification(message),SMSNotification(message),PushNotification(message)]
run_notification(notifications)