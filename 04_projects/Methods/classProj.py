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