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
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("Division by zero is not allowed")

# try: 
#     num=int("abc")
#     result=10/num
# except ValueError:
#     print("Invalid input! Please enter a number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")

# try: 
#     num=int("4a")
# except ValueError:
#     print("Conversion failed")
# else:
#     print("Conversion successfull: ",num)
# finally:
#     print("This block always runs.")

# # Challenges

# # Level 1
# # Write a program that asks for a number and divides 100 by it.
# divisor=input("Enter a number to divide 100: ")
# try:
#     result=100/float(divisor)
# except ValueError:
#     print("The divisor must be a number!")
# except ZeroDivisionError:
#     print("Division by zero is invalid!")
# else:
#     print(f"The division of zero by {divisor} is {result}")

# # Level 2
# # Open a file entered by the user.
# file_name=input("Enter file name to be accessed: ")
# try:
#     with open(file_name,"r") as f:
#         f.read()
# except FileNotFoundError:
#     print(f"The file {file_name} doesn't exist!")
# else:
#     print(f"The file {file_name} found")
# finally:
#     print(f"Search was for {file_name}")

# # level 3
# # Created a function check_age(age) that raises a ValueError if age < 0
# def check_age(age):
#     if age<0:
#         raise ValueError("Age cannot be negative!")
#     else:
#         print(f"{age} is valid age")
# try:
#     age=int(input("Enter the age: "))
#     check_age(age)
# except ValueError as e:
#     print("Error: ",e)

# Level 4
# Define a custom exception class (e.g. NegativeBalanceError).
# Write a banking simulation where withdrawing more than the balance raises this exception.
# Handle it gracefully with a message.
class NegativeBalanceError(Exception):
    """Raised when withdrawal amount exceeds available balance."""
    def __init__(self,balance,amount):
        super().__init__(f"Attempted withdrawal of {amount} with balance {balance}.")
        self.balance=balance
        self.amount=amount
class Account:
    def __init__(self,balance=0):
        if balance<0:
            raise NegativeBalanceError(balance,0)
        self.balance=balance
    def deposite(self,amount):
        if amount<0:
            raise ValueError("Deposite amount cannot be negative.")
        self.balance+=amount
        print(f"Desposited {amount}. New balance : {self.balance}")
    def withdraw(self,amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise NegativeBalanceError(self.balance,amount)
        self.balance-=amount
        print(f"Withdrew {amount}. Remaining balace: {self.balance}")
try:
    account=Account(180)
    account.withdraw(150)
    account.deposite(-200)
except NegativeBalanceError as e:
    print("Error: ",e)