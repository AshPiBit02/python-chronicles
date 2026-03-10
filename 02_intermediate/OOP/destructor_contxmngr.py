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
# class Demo:
#     def __init__(self,name):
#         self.name=name
#         print(f"Object {self.name} created")
#     def __del__(self):
#         print(f"Destructor called, object {self.name} deleted")
# d=Demo("test")
# del d # delete object explicitly

#    # File handling
# class FileHandler:
#     def __init__(self,filename):
#         self.file=open(filename,"w")
#         print("File opened")
#     def write(self,text):
#         self.file.write(text)
#     def __del__(self):
#         self.file.close()
#         print("File closed automatically")
# f=FileHandler("demo.txt")
# f.write("This is a demo file")

# Context Manager
   # a Python construc that allows you to set up and clean up resources automatically.
   # is most commonly used with the "with" statement.
   # Purpose: ensure that resources(like files, database connections, locks) are properly released, even if errors occur.
   # Uses:
        # File handling: automatically close files after use.
        # Database connections: ensure connections are closed safely.
        # Threading/locks: acquire and release locks without forgetting.
        # Temporary changes: apply a setting for block of code, then restore it.
   # Essential Elements:
        # __enter__ method
            # runs when the "with" block starts.
            # sets up the resource and returns it.
        # __exit__ method
            # runs when the "with" block ends(whether normally or due to an error)
            # cleans up the resource.
            # receives exception details if an error occurred inside the block.
        # with statement
            # ensures __enter__ and __exit__ are called automatically. 
# Examples:
   # File Handling with Context Manager
class FilehandlerCM:
    def __init__(self,filename):
        self.filename=filename
    def __enter__(self):
        self.file=open(self.filename,"w")
        print("File opened")
        return self.file # returned object is assigned to variable in 'with'
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.file.close()
        print("File closed safely")
with FilehandlerCM("demoCM") as f:
    f.write("Hello, this file belongs to context manager")