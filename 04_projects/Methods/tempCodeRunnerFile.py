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

# Level 3 (Class state and Factories)
  # Register Factory
     # Create a 'Plugin' class with class attribute registry={}.
     # Add '@classmethod register(cls,name,plugin_cls) to store plugin_cls' in 'registry'.
     # Add '@classmethod create(cls,name,*args,**kwargs)' that instantiates the registered plugin class.
class Plugin:
    registry={}
    @classmethod
    def register(cls,name,plugin_cls):
        """Register a plugin class under a given name."""
        if name in cls.registry:
            raise ValueError(f"Plugin '{name}' already registered.")
        cls.registry[name]=plugin_cls
        return f"Plugin '{name}' registered."
    @classmethod
    def create(cls,name,*args,**kwargs):
        if name not in cls.registry:
            raise ValueError(f"No plugin registered under '{name}'.")
        return cls.registry[name](*args,**kwargs)
    @classmethod
    def list_plugins(cls):
        """Return a list of all registered plugin names."""
        return list(cls.registry.keys())
class LoggerPlugin:
    def __init__(self,level="INFO"):
        self.level=level
    def run(self):
        return f"Logging at {self.level} level."
class AuthPlugin:
    def __init__(self,user):
        self.user=user
    def run(self):
        return f"Authenticating user {self.user}."
#Register plugins
print(Plugin.register("logger",LoggerPlugin))
print(Plugin.register("auth",AuthPlugin))

# List available plugins
print(Plugin.list_plugins())

# Create instances dynamically
logger=Plugin.create("logger",level="DEBUG")
print(logger.run()) 
# Logging at DEBUG level.

auth=Plugin.create("auth",user="ashpibit")
print(auth.run())        
# Authenticating user ashpibit

"""Versioned Constructor"""
# Create a 'Document' class with 'content' and 'version'.
# Add @classmethod new_version(cls,content) that returns a 'Document' with 'version' increment from a class counter.
class Document:
    version_counter=2.0
    def __init__(self,content,version):
        self.content=content
        self.version=version
    @classmethod
    def new_version(cls,content):
        cls.version_counter+=.1
        return cls(content,cls.version_counter)
    @classmethod 
    def current_version(cls):
        return cls.version_counter
# Create first document
doc1=Document.new_version("Initial draft")
print(doc1.version,doc1.content)
# 1 Initial draft

# Create second document
doc2=Document.new_version("Edited draft")
print(doc2.version,doc2.content)
# 2 Edited draft

# Check current version counter 
print(Document.current_version())

"""Level 4 (Real World Challenge)"""
# BankAccount with Global settings
   # Create 'BankAccount' with instance attributes 'owner' and 'balance'.
   # Add class attribute 'default_currency="USD"' and 'interest_rate=0.01'.
   # Implement @classmethod set_currency(cls,currency) and @classmethod set_interest_rate(cls,rate).
   # Implement @classmethod from_dict(cls,data) as alternate consructor that respects default_currency if data lacks currency.
class BankAccount:
    default_currency="USD"
    interest_rate=0.01
    def __init__(self,owner=None,balance=0.0,currency=None):
        self.owner=owner
        self.balance=float(balance) 
        self.currency=currency if currency is not None else self.__class__.default_currency
    @classmethod
    def set_currency(cls,currency):
        cls.default_currency=currency
        return f"Default currency set to {cls.default_currency}"
    @classmethod
    def set_interest_rate(cls,rate):
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        cls.interest_rate=float(rate)
        return f"Interest rate set to {cls.interest_rate}"
    
    """Alternate constructor"""
    @classmethod
    def from_dict(cls,data):
        owner=data.get("owner")
        if not owner:
            raise ValueError("Owner is required to create a BankAccount.")
        balance=data.get("balance",0.0)
        currency=data.get("currency",None) # None -> constructor will use default 
        return cls(owner,balance,currency)
    def deposit(self,amount):
        if amount < 0:
            raise ValueError("Negative amount!")
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount <=0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance-=amount
        return self.balance
    def apply_interest(self):
        self.balance+=self.balance*self.__class__.interest_rate
        return self.balance
    
    def __str__(self):
        return f"BankAccount(owner= {self.owner}  balance= {self.balance:.2f} {self.currency}"
print('-'*40)
data={"owner":"ashpibit","balance":9001.0,"currency":"GBP"}
print(BankAccount.default_currency)
print(BankAccount.interest_rate)

print(BankAccount.set_currency("EURO"))
print(BankAccount.set_interest_rate(0.2))

a1=BankAccount("ash",2000)
a2=BankAccount.from_dict(data)

print(a1)
print(a2)

a1.deposit(200)
a1.withdraw(100)
a1.apply_interest()
print(a1.balance)

# Multi Format Factory
  # Create Event class with name, date, location.
  # Implement @classmethod from_iso(cls,iso_string) and @classmethod from_json(cls,json_str) to prase different input formats and return Event instances.
import json
from datetime import datetime, date, time
class Event:
    def __init__(self,name:str,date_time:datetime,location: str=None):
        if not name:
            raise ValueError("Event name is required.")
        if not isinstance(date_time,datetime):
            raise TypeError("date_time must be a datetime.datetime instance.")
        self.name=name
        self.data_time=date_time
        self.location=location
    @classmethod
    def from_iso(cls,iso_string:str,location: str=None):
        if not iso_string or not isinstance(iso_string,str):
            raise ValueError("iso_string must be a non-empty string.")
        # allow both 'T' and space separators; datetime.fromisoformat handles both
        try:
            # if only date is provided, convert to midnight datetime
            if len(iso_string.strip())==10 and iso_string.count("-")==2:
                dt=datetime.fromisoformat(iso_string).replace(hour=0,minute=0,second=0,microsecond=0)
            else:
                dt=datetime.fromisoformat(iso_string)
        except Exception as exc:
            raise ValueError(f"Invalid ISO datetime string: {iso_string}") from exc
        # Name must be provided separately by caller or inferred; here we require name in iso path
        # For convenience, use a defualt name derived from date if caller omitted name
        default_name = f"Event on {dt.date().isoformat()}"
        return cls(default_name,dt,location)
    
    @classmethod
    def from_json(cls,json_str:str,):
        if not json_str or not isinstance(json_str,str):
            raise ValueError("json_str must be a non-empty string.")
        try:
            data=json.loads(json_str)
        except json.JSONDecodeError as exc:
            raise ValueError("Invalid JSON string.") from exc
        name=data.get("name")
        if not name:
            raise ValueError("JSON musst include 'name' field.")
        # Accept either 'date_time' or 'date'
        dt_value= data.get("date_time") or data.get("date")
        if not dt_value:
            raise ValueError("JSON must include 'date_time' or 'date' field.")
        # Prase date or datetime
        try:
            if isinstance(dt_value,(int,float)):
                # treat numeric as timestamp(seconds)
                dt=datetime.fromtimestamp(dt_value)
            elif isinstance(dt_value,str):
                # If onlyo date provided, convert to midnight
                if len(dt_value.strip())==10 and dt_value.count("-")==2:
                    dt=datetime.fromisoformat(dt_value).replace(hour=0,minute=0,second=0,microsecond=0)
                else:
                    dt=datetime.fromisoformat(dt_value)
            else:
                raise ValueError("Unsupported date format in JSON.")
        except Exception as exc:
            raise ValueError(f"Invalid date/time value: {dt_value}") from exc
        location=data.get("location")
        return cls(name,dt,location)
    def is_past(self):
        """Return True if the event datetime is before now."""
        return self.date_time < datetime.now()
    def summary(self):
        """Human readable one-line summary."""
        loc=f" at {self.location}" if self.location else""
        return f"{self.name} on {self.date_time.isoformat()} {loc}"
    def __str__(self):
        return self.summary()
    def show_attrs(self):
        """Return instance attributes as a dict for debugging."""
        return {"name": self.name,"date_time": self.date_time.isoformat(),"location": self.location}
# From ISO datetime string(explicit time)
e1=Event.from_iso("2026-03-14T09:00:00",location="Kahandu")

# From ISO date only (defaults to midnight and uses defualt name)
e2=Event.from_iso("2026-03-14")
print(e2.show_attrs())
