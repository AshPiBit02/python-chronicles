# Destructor
   # a special method in Python named __del__.
   # is automatically called when an object is about to be destroyed(usually when it goes out of scope or you explicitly delete it).
   # Purpose: perform cleanup tasks before the object is removed from memory.
   # Uses:
        # Resource cleanup: close files, release database connections, free memory.
        # Logging/debugging: track when objects are deleted.
        # Automatic housekeeping: remove temporary data or notify when an object's lifecycle ends.
   # Essential Elements of Destructor
        # Method name: __del__
        # Self parameter: always takes self(the current object)
        # Automatic call: invoked by Python's garbage collector when the object is deleted.
        # Limitations:
              # Timing is not guranteed(depends on garbage collection.)
              # Exceptions inside __del__ are ignored.
              # Circular references may prevent destructors from running.
# Example:
   # simple destructor
class Demo:
    def __init__(self,name):
        self.name=name
        print(f"Object {self.name} created")
    def __del__(self):
        print(f"Destructor called, object {self.name} deleted")
d=Demo("test")
del d # delete object explicitly

   # File handling
class FileHandler:
    def __init__(self,filename):
        self.file=open(filename,"w")
        print("File opened")
    def write(self,text):
        self.file.write(text)
    def __del__(self):
        self.file.close()
        print("File closed automatically")
f=FileHandler("demo.txt")
f.write("This is a demo file")
