# Descriptors
"""
Intro: 
       A protocol(__get__,__set__,__delete__) for controlling attribute behavior.
       Properties are a special case of descriptors.

Problem solved:
       Reusable attribute logic across multiple classes.
       Frameworks use them to map attributes to DB fields or enfore rules.

Where used: 
       Django ORM, SQLAlchemy.
       Validation libraries.
       Behind property, staticmethod,classmethod.

Alternative:
       Properties(simpler, but less reusable)
       Manual getter/getter
"""
# Examples

""" Without descriptor(manual validation in every class)"""
class manual_BankAccount:
    def __init__(self,balance=0):
        if balance < 0: raise ValueError("Invalid balance!")
        self.balance=balance
class manual_Wallet:
    def __init__(self,amount=0):
        if amount < 0: raise ValueError("Invalid Amount!") # Repeated logic
        self.amount=amount
ab=manual_BankAccount(5050)
mw=manual_Wallet(202)
print(f"{ab.__dict__}\n{mw.__dict__}")
# bc=manual_BankAccount(-5050) -> raise error



print('-'*40)
""""With descriptor(reusable logic)"""
class PositiveValue:
    def __set_name__(self,owner,name): # owner -> class(BankAccount/Wallet), name -> attribute(balance/amount)
        self.name=name
    def __get__(self,inst,owner):
        return inst.__dict__.get(self.name,0) # zero is default
    def __set__(self,inst,val):
        if val < 0:
            raise ValueError("Entered value must be positive!")
        inst.__dict__[self.name]=val
class BankAccount:
    balance=PositiveValue()
    def __init__(self,balance=0):
        self.balance=balance
class Wallet:
    amount=PositiveValue()
    def __init__(self,amount=0):
        self.amount=amount
acc=BankAccount(100)
acc.balance=400
print(acc.__dict__)
# acc.balance=-200 -> raise error
ww=Wallet()
print(ww.__dict__)
ww.amount=222
print(ww.amount)
print(ww.__dict__)
# ww.amount=-2 -> raises error

