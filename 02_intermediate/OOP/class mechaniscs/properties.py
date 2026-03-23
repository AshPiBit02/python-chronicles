#   Properties
"""
Intro:
     A way to manage attributes access with logic while still using simple dot syntax(obj.attr).
     Built on descriptors internally.
    
Problem solved:
     Avoids clunky get_x()/set_x() methods.
     Lets you add validation or computed values without changing how attributes are accessed.

Where Used: 
     Validation(e.g. balance>=0)
     Computed attributes(full_name)
     Encapsulation in OOP

Alternative: 
     Explicit getter/setter methods.
     Direct public attributes(no control).
     Descriptors(lower-level).
     
"""
# Examples:

# Without using property(manaul getter/setter)
class Manul_BankAccount:
    def __init__(self,balance=0):
        self._balance=balance
    def get_balance(self):
        return self._balance
    def set_balance(self,amount):
        if amount<0:
            raise ValueError("Invalid Amount")
        self._balance=amount
ac=Manul_BankAccount(500)
print(ac.get_balance())
ac.set_balance(1000)
print(ac.get_balance())

# With property
class Advanced_BankAccount:
    def __init__(self,balance=0):
        self._balance=balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,amount):
        if amount < 0 : raise ValueError("Invalid Amount!")
        self._balance=amount
aac=Advanced_BankAccount(500)
print(aac.balance)
aac.balance=555
print(aac.balance)

    
