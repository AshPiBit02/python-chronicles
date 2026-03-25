from base import NotifierFactory
nf=NotifierFactory()
sms=nf.get_notifier("sms")
sms.send("Your OTP is 1474")
push=nf.get_notifier("push")
push.send("You have received 10 new messages","urgent")
try:
    uk=nf.get_notifier("unknown")
    uk.send("unknown message")
except ValueError as e:
    print("Error: ",e)
broadcast=nf.get_notifier("all")
for info in broadcast:
    info.send("Alert! Earthquake within 5 minutes, Stay away from high structures!!!","urgent")
email=nf.get_notifier("email")
email.send("Offer letter from FAANG!")