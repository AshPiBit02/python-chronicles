import datetime as dt
class Logger:
        @staticmethod
        def log(message,channel,priority):
                dt_format=dt.datetime.now().replace(microsecond=0).isoformat()
                log_entry=f"{dt_format} | {channel.upper()} | {message} | {priority.upper()} "
                print(f"[LOG] {log_entry}")
                with open("notification_log.txt","a") as f:
                    f.write(log_entry+"\n")
class Notifier:
    def send(self,message,priority="normal"):
        raise NotImplementedError("Subclasses must implement send()")

class EmailNotifier(Notifier):
    def send(self,message,priority="normal"):
        if priority=="urgent":
            print(f"Sending Email(Urgent): {message}")
        else:
            print(f"Sending Email: {message}")
        Logger.log(message,"Email",priority)

class SMSNotifier(Notifier):
    def send(self,message,priority="normal"):
        if priority=="urgent":
            print(f"Sending SMS(Urgent): {message}")
        else:
            print(f"Sending SMS: {message}")
        Logger.log(message,"SMS",priority)

class PushNotifier(Notifier):
    def send(self,message,priority="normal"):
        if priority=="urgent":
            print(f"Sending Push(Urgent): {message}")
        else:
            print(f"Sending Push Notification: {message}")
        Logger.log(message,"Push",priority)


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


