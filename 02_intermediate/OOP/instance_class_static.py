# Instance 
   # These methods are functions defined inside a class whose first parameter is conventionally named 'self'.
   # When you call the method on an object, 'self' refers to that specific instance, giving the method access to the instance's attributes and other methods.
   # Uses:
        # Model object behavior: implement actions that depend on an object's state(e.g. 'account.deposit').
        # Read and update instance attributes: change 'self.balance','self.status', etc.
        # Coordinate multiple attributes: compute values derived from several instance fields.
        # Encapsulate logic: keep related behavior inside the class for clarity and reuse.
   # Key Elements:
      # Method signature: first parameter must be 'self'(or another name, but self is standard)
      # Defined insided class body: indented under class.
      # Called on instances: 'obj.method(...)' - python binds 'obj' to 'self'.
      # Can access 'self' attributes and other instance methods.
      # Can return values or mutate the instance.
# Examples

  # Minimal
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        return f"Hi, I'm {self.name}"
    def have_birthday(self):
        self.age+=1
        return self.age
p=Person("Aashish",21)
print(p.greet())
print(p.have_birthday())

  # Validation and State Change
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        if amount <=0:
            raise ValueError("Invalid amount!")
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance-=amount
        return self.balance
try:
     acct=BankAccount("cjbtk",500)
     print(acct.deposit(100))
     print(acct.deposit(10))
     print(acct.withdraw(1000))
except ValueError as e:
    print("Error: ",e)