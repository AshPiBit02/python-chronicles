# Exception handling in Python is a way to manage runtime errors gracefully.
# Usage :
   # Prevent crashes: handle errors without stopping the program.
   # Provide feedback: Show user-friendly messages.
   # Ensure cleanup: close files, release resources, or reset states.
   # Control flow: Decide what happens next when something goes wrong.
# Syntax:  
    # try:
       # code that may cause an error
    # except ExceptionType:
       # code to handle the error
    # else:
       # code that runs if no error occurs
    # finally: 
       # code that always runs (cleanup)
# Examples:
try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero is not allowed")

try: 
    num=int("abc")
    result=10/num
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

try: 
    num=int("4a")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successfull: ",num)
finally:
    print("This block always runs.")