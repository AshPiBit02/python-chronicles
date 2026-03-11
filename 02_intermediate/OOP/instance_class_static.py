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


print('*'*40)

# Class Method
  # a method that operates on the class itself, not on individual objects.
  # receives the class as its first argument, conventionally named 'cls'.
  # declared with the '@classmethod' decorator.
  # Purpose: work with class-level data, provide alternate constructors, or define behavior that applies to the class as a whole.
  # Uses:
       # Modify class variables -> change values shared across all instances.
       # Alternate constructors -> create objects in different ways(e.g. from a dictionary, JSON, or database row).
       # Factory methods -> encapsulate complex object creation logic.
       # Class-wide operations -> perform tasks that affect the class rather than a single object.
  # Key Elements:
       # Decorator: '@classmethod' must be placed above the method definintion.
       # First  parameter: 'cls', representing the class itself.
       # Access: can read and modify class atrributes, but not instance attributes directly.
       # Call style: can be called on the class (Class.method(..)) or on an instance(obj.method(...)), but always receives the class as 'cls'.
# Example
  # Modify class varibles
class BankAccount:
    interest_rate=0.2 # class variable shared by all accounts
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    @classmethod
    def set_intereset_rate(cls,rate):
        cls.interest_rate=rate
BankAccount.set_intereset_rate(0.05)
print(BankAccount.interest_rate)

  # Alternate Constructor
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    @classmethod
    def from_dict(cls,data):
        return cls(data["owner"],data["balance"])
data={"owner":"Aashish","balance":2500000}
a=BankAccount("dj",1)
ac=BankAccount.from_dict(data)
print(ac.owner,ac.balance)

class StudentInfo:
    count=0
    total_gpa=0
    def __init__(self,roll_no,name,gpa):
        self.name=name
        self.roll_no=roll_no
        self.gpa=gpa
        StudentInfo.count+=1
        StudentInfo.total_gpa+=gpa
    @classmethod
    def get_student_count(cls):
        return f"Total no of student: {cls.count}"
    @classmethod
    def get_avg_gpa(cls):
        if cls.count==0:
            return 0
        else:
            return f"Average gpa : {cls.total_gpa/cls.count:.2f}"
stu1=StudentInfo(1,"John",3.96)
stu2=StudentInfo(2,"Snow",2.8)
stu2=StudentInfo(3,"Arry",2.0)
print(StudentInfo.get_student_count())
print(StudentInfo.get_avg_gpa())

# Static Method
   # a method inside a class that does not take 'self' or 'cls' as its first argument.
   # Declared with the '@staticmethod' decorator.
   # Purpose: group uitility functions inside a class's namespace, even though they don't depend on instance or class data.
   # They behave just like normal functions, but live inside the class for logical organization.
   # Uses: 
       # Uitlity/helper functions: calculations, validations, or transformations related to the class.
       # Organizational clarity: keep related functions inside the class rather than floating in a module.
       # Independent logic: when the function doesn't need to access instance(self) or class(cls) attributes.
       # Code reusablility: makes it clear the function beglongs conceptually to the class.
   # Key Elements 
       # Decorator: '@staticmethod' must be placed above the method definition.
       # No automatic first argument: unlike instance(self) or class(cls) methods.
       # Call style: can be called on the class(Class.method(...)) or on an instance(obj.method(...)), but neither self nor cls is passed.
       # Behavior: acts like plain function, but namespaced inside the class.
       