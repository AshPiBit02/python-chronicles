# Singleton Design Pattern
"""
    The singleton pattern ensures that a class has only one instance throughout the program and
      provides a global points of access to it.

    Intent:
       -> Control object creation so that only one instance exists, avoiding duplication and inconsistency.
    
    Use Cases:
       -> Database connections(only one connection manager should exist).
       -> Logging systems(centralized logger)
       -> Configuration managers(single source of truth for settings).
       -> Thread pools or caches.

"""
# Examples

"""
 Problem Without Singleton
  -> Imaging a logging system where multiple parts of your program create their own objects independently.
"""
class Logger:
    def __init__(self):
        print("Logger created")
    def log(self,message):
        print(f"LOG: {message}")
logger1=Logger()
logger2=Logger()
logger1.log("First Message")
logger2.log("Second Message")
print(logger1 is logger2)
"""
Problem: 
    i. multiple loggers exist -> inconsistent logging.
    ii. Each logger may have different settings -> chaos in large systems.
    iii. Wasted resources(duplicate objects doing the same job). 
"""

""" Solution With Singleton """
class SingletonLogger:
    _instance=None
    def __new__(cls,*args,**kwargs): # *args and **kwargs allows the method to accept any kind of arguments without knowing in advance what they'll be
        if cls._instance is None:
            cls._instance=super().__new__(cls) # object is create if none exist previously
            print("Logger created")
        return cls._instance
    def log(self,message):
        print(f"LOG: {message}")
logger1=SingletonLogger()
logger2=SingletonLogger()
logger1.log("First message")
logger2.log("Second message")
print(logger1 is logger2)

"""
  Only one logger is created.
  All parts of the program share the same instance.
  Centralized configuration and consistent logging.
"""