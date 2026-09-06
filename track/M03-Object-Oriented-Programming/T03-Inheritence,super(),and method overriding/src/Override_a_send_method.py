class Notification:
    def send(self,message):
        print("General Notification:",message)


class Email(Notification):
    def send(self,message):
        print("Email Notification:",message)

message=input()
n=Notification()
n.send(message)
e=Email()
e.send(message)
