# Hands-On Projects using class method

# Level 1(Basic)
  # Shared Counter
    # Create a 'Visitor' class with a class attribute count=0.
    # Add a '@class method incretement()' that increases count by 1.
    # Add a '@clasmethod current_count()' that returns the current 'count'.
class Visitor:
    count=0
    @classmethod
    def increment(cls):
        """Increment the shared visitor count by 1"""
        cls.count+=1
        print("Count incremented")
    @classmethod
    def current_count(cls):
        return cls.count
    @classmethod
    def reset(cls):
        cls.count=0
Visitor.increment()
Visitor.increment()
print(Visitor.current_count())
Visitor.increment()
print(Visitor.current_count())
Visitor.reset()
print(Visitor.current_count())
  # Configuration Holder
    # Create a AppConfig class with class attributes debug=False and version="2.0"
    # Add a '@classmethod' set_debug(flag)' to change debug.
    # Add a '@classmethod info()' that returns a dict of class settings.
class AppConfig:
    debug=False
    version="2.0"
    @classmethod
    def set_debug(cls,flag:bool):
        cls.debug=bool(flag)
        return f"Debug mode set to {cls.debug}"
    @classmethod
    def info(cls):
        return {"debug": cls.debug,"version": cls.version}
    @classmethod
    def set_version(cls,version:str):
        cls.version=version
        return f"Version updated to {cls.version}"
print(AppConfig.info())
AppConfig.set_version("2.1")
AppConfig.set_debug(True)
print(AppConfig.info())

# Level 2(Alternate Constructors)
  # From Dictionary
    # Create a User class with username and email.
    # Implement @classmethod from_dict(cls,data) that returns a User from {"username":....,"email":.....}.
class User:
    def __init__(self,username=None,email=None):
        self.username=username
        self.email=email
    @classmethod
    def from_dict(cls,data):
        return f"username: {data["username"]}\nemail: {data["email"]}"
data={"username":"ashpibit","email":"aashishcharudhari249@gmail.com"}
print(User.from_dict(data))
  # Create a Product class with name and price.
  # Implement @classmethod from_csv(cls,line) where line is "name,price" and return a Product.
class Product:
    def __init__(self,name=None,price=0):
        self.name=name
        self.price=price
    @classmethod
    def from_csv(cls,line: str):
        parts=line.strip().split(",")
        if len(parts)!=2:
            raise ValueError("CSV line must contain exactly two values: name, price")
        name,price=parts
        return cls(name,price)
    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"
P1=Product("Laptop",120000)
print(P1)
line="Phone,70000"
p2=Product.from_csv(line)
print(p2)
bad_line="InvalidLine"
try:
    p3=Product.from_csv(bad_line)
except ValueError as e:
    print("Error: ",e)