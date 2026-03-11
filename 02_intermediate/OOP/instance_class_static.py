# Instance Method
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
    def transfer(self,amount,other):
        self.withdraw(amount)
        other.deposit(amount)
    # __str__(self) -> a special method that defines how your object is represented as a string. Automatically runs when you call str(obj) or print the object.
    def __str__(self):
        print('-'*40)
        return f"Owner: {self.owner} \n Balance: ${self.balance}"
try:
     acct=BankAccount("account0",5000)
except ValueError as e:
    print("Error: ",e)

try:
    acct1=BankAccount("account1",1000)
except ValueError as e:
    print(f"Error: {e}")

try:
    acct.transfer(2000,acct1)
except ValueError as e:
    print(f"Error: {e}")
print(acct1.balance)
print(acct.balance)

try:
    acct.transfer(1500,acct1)
except ValueError as e:
    print(f"Error: {e}")
print(acct1.balance)
print(acct.balance)

# vars(self) a built-in function that returns the __dict__ of an object
print(vars(acct))
print(vars(acct1))

print(acct)
print(acct1)
print(str(acct))




# Class Method
  # a method that operates on the class itself, not on individual oibjects.
  # receives the class as its first argument, conventionally named 'cls'.
  # declared with the '@classmethod' decorator.
  # Purpose: work with class-level data, provide alternate constructors, or define behavior that applies to the class as a whole.
  # Uses:
       # Modify class variables -> change values shared across all instances.
       # Alternate constructors -> create objects in different ways(e.g. from a dictionary, JSON, or database row).
       # Factory methods -> encapsulate complex object creation logic.
       # Class-wide operations -> perform tasks that affect the class rather than a single object.