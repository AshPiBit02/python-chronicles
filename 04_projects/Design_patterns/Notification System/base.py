class Notifier:
    def send(self,message,priority="normal"):
        raise NotImplementedError("Subclasses must implement send()")

class EmailNotifier(Notifier):
    def send(self,message,priority="normal"):
        if priority=="urgent":
            print(f"Sending Email(Urgent): {message}")
        else:
            print(f"Sending Email: {message}")

class SMSNotifier(Notifier):
    def send(self,message,priority="normal"):
        if priority=="urgent":
            print(f"Sending SMS(Urgent): {message}")
        else:
            print(f"Sending SMS: {message}")

class PushNotifier(Notifier):
    def send(self,message,priority="normal"):
        if priority=="urgent":
            print(f"Sending Push(Urgent): {message}")
        else:
            print(f"Sending Push Notification: {message}")

class NotifierFactory:
    @staticmethod
    def get_notifier(send_through):
        if send_through=="email":
            return EmailNotifier()
        elif send_through=="sms":
            return SMSNotifier()
        elif send_through=="push":
            return PushNotifier()
        elif send_through=="all": # multi-channel broadcast
            return ([EmailNotifier(),SMSNotifier(),PushNotifier()])
        else:
            raise ValueError("Unknown Notifier!")


