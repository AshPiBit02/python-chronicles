""" Context Manager """
  # a constructor that set up and tear down resources automatically.
  # most commonly used the 'with' statement
  # Use:
    # ensure proper resource management(file,network connections,locks)
    # automatically handle setup and cleanup without nedding to remember
    # make code safer and cleaner by guaranteeing cleanup even is an error occurs.
  # Key Elements:
    # __enter__ -> defines what happens when the context start(when 'with' is entered)
    # __exit__ -> defines what happens when the context ends(when 'with' block finishes, even if there's an error)
  # Examples:

# 1. File Handling(built-in context manager)
with open("data.txt","a") as f:
    f.write("Hello, Boy!")
""" File is automatically closed after the block 
      Here, open() returns a context manager.
       __enter__ -> opens the file.
       __exit__ -> closes the file safely.
"""

# 2. Custom Context Manager
class DemoContext:
    def __enter__(self):
        print("Entering context...")
        return "Resource ready"
    def __exit__(self,exc_type,exc_value,traceback):
        print("Exiting context...")
        # Returning False means exceptions are not suppressed
        return False
with DemoContext() as resource:
    print(resource)

# 3. Using contextlib
from contextlib import contextmanager
@contextmanager
def simple_context():
    print("Setup")
    yield "Resource" # yield truns a function into a generator that produces values one at a time
    print("Cleanup")
with simple_context() as r:
    print(r)