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