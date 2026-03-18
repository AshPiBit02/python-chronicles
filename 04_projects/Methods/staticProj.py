"""Hands-On projects using static method"""
# Level 1 
  # 1. Expense Tracker
     # Class: Expense
     # Static method: validate_amount(amount) -> ensures amount > 0
     # Instance: stores category, amount, date.
     # Real use: track daily spending safely.
from datetime import date
class Expense:
    def __init__(self,category:str,amount:float,spent_on: date = None, note:str=None):
        if not Expense.validate_amount(amount):
            raise ValueError("Amount must be a positive number.")
        """not isinstance ensures if category is a string and not category.strip() rejects strings taht are empty or only whitespace."""
        if not isinstance(category,str) or not category.strip(): 
            raise ValueError("Category must be a non-empty string.")
        self.category=category.strip()
        self.amount=float(amount)
        self.spent_on=spent_on or date.today()
        self.note=note
    @staticmethod
    def validate_amount(amount) -> bool: # -> (return type ammontation) is a type hint that indicates what type of value the functio return
        if amount is None:
            return False
        if isinstance(amount,str):
            try: 
                amount=float(amount)
            except ValueError:
                return False
        if not isinstance(amount,(int,float)):
            return False
        return amount > 0
    def to_dict(self) -> dict:
        return{
            "category":self.category,
            "amount":self.amount,
            "spent_on":self.spent_on.isoformat(),
            "note":self.note,
        }
    """r! tells python to use repr(){similar to __str__ but is shows exact contents including escape characters.} on that value before formatting it into the string"""
    """Example: print(str("Hello\nWorld))-> Hello(in one line) then World(in next line) and print(repr("Hello\nWorld")) -> 'Hello\nWorld' """
    def __repr__(self):
        return f"Expense(category={self.category!r}, amount={self.amount:.2f}, spent_on={self.spent_on}, note={self.note!r})"
# Valid expenses
e1=Expense("Food",12.5)
e2=Expense("Transport","3.20",note="Bus fare")
# Invalid amount raise
try: 
    Expense("Misc",0)
except ValueError as e:
    print("Error: ",e)
# quick validation without creating an instance
print(Expense.validate_amount(5))        
print(Expense.validate_amount("0"))        
print(Expense.validate_amount("-3.5"))        
print(Expense.validate_amount("abc"))        
    
  # 2. Temperature Converter
     # Class: Temperature
     # static method: c_to_f(celsius), f_to_c(fahrenheit)
class Temperature:
    @staticmethod
    def c_to_f(celsius):
        if not isinstance(celsius,(int,float,str)):
            raise ValueError("Invalid value!")
        try:
            celsius=float(celsius)
        except ValueError:
            raise ValueError("Invalid value!")
        return f"{float(celsius)}F -> {float((1.8*celsius)+32)}F"
    @ staticmethod
    def f_to_c(fahrenheit):
        if not isinstance(fahrenheit,(int,float,str)):
            raise ValueError("Invalid value!")
        try:
            fahrenheit=float(fahrenheit)
        except ValueError:
            raise ValueError("Invalid value!")
        return f"{float(fahrenheit)}F -> {float((5/9)*(fahrenheit-32)):.2f}C"
try:
    print(Temperature.c_to_f(25))
except ValueError as e:
    print("Error: ",e)
try:
    print(Temperature.c_to_f("100"))
except ValueError as e:
    print("Error: ",e)
try:
    print(Temperature.f_to_c(25))
except ValueError as e:
    print("Error: ",e)

# Level 2
  # 3. Email Utitlity
     # Class: EmailHelper
     # static method: validate_email(email) -> checks format with regex, mask_email(email) -> hides part of the address of privacy.
     # Real use: safe handling of user emails.
import re
class EmailHelper:
    @staticmethod
    def validate_email(email) -> bool:
        pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        return re.match(pattern,email) is not None
    def mask_email(email) -> str:
        at_index=email.find("@")
        visible=email[:3]
        masked_local=visible + "*" * (at_index-3)
        return masked_local + email[at_index:]
print(EmailHelper.validate_email("aashishchaudahr234@gmail.com"))
print(EmailHelper.mask_email("aashishchaudahr234@gmail.com"))


  # 4. Password Checker
     # Class: PasswordUtils
     # Staic methods: is_strong(password) -> checks length,digits,uppercase, symbols, hash_password(password) -> returns a hased version.
     # Real use: secure user authentication.
import hashlib
import re
class PasswordUtils:
    @staticmethod
    def is_strong(password:str) -> bool:
        if not isinstance(password,str):
            return False
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]",password):
            return False
        if not re.search(r"[a-z]",password):
            return False
        if not re.search(r"\d",password): # checks if password contains at least one digit
            return False
        if not re.search(r"[!@#$%^&*(),.?\/.:{}|<>]",password):
            return False
        return True
    @staticmethod
    def hash_password(password:str) -> str:
        if not isinstance(password,str):
            raise ValueError("Password must be a string.")
        """.hexdigest return a human-readable string of hex characters"""
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
print(PasswordUtils.is_strong("abc"))
print(PasswordUtils.is_strong("Abc123&!tr"))
hashed=PasswordUtils.hash_password("Abc123&3,s")
try:
    print(hashed)
except ValueError as e:
    print("Error: ",e)
    
        

# Level 3
  # 5. File Utility
     # Class: FileUtils
     # Static methods: get_extension(filename), is_valid_filename(filename)
     # Real use: validate and process uploaded files.
print('-'*40)
import os
import re
class FileUtils:
    @staticmethod
    def get_extension(filename:str) -> str:
        """
        Return the file extension without the dot.
        Example: example.json -> json
        """
        if not isinstance(filename,str) or not filename.strip(): # if filename.strip() is empty python treats it as False
            raise ValueError("File name must be a non-empty string.")
        _, ext=os.path.splitext(filename)
        return ext[1:] if ext else ""
    """
    os.path.splitext(filename) -> splits a filename into two parts(part before dot & after including dot)
    _ is a throwaway variable -> it captures the root part but we don't need it.(we can define any varible that place of _)
    return ext[1:] if ext else "" -> returns the part after dot if ext contain second part else it returns empty string.
    """
    @staticmethod
    def is_valid_filename(filename:str) -> bool:
        if not isinstance(filename,str) or not filename.strip():
            return False
        forbidden=r'[\\/:*?"<>|]'
        if re.search(forbidden,filename):
            return False
        if not FileUtils.get_extension(filename):
            return False
        return True
try:
    print(FileUtils.get_extension(""))
except ValueError as e:
    print("Error: ",e)
print(FileUtils.get_extension("report.pdf"))     # pdf
print(FileUtils.get_extension("archive.tar.json")) # gz
print(FileUtils.get_extension("noext"))          # ""
print(FileUtils.is_valid_filename("report.txt")) # True
print(FileUtils.is_valid_filename("bad|name.txt")) # False
print(FileUtils.is_valid_filename("noext"))    
                  
  # 6. Math Helper
     # Class: MathUtils
     # Static Methods: is_prime(n), factorial(n)
     # Real use: reusable math utilities in apps.
print('-'*50)
class MathUtils:
    @staticmethod
    def is_prime(num:int) -> bool:
        if not isinstance(num,int) or num < 2:
            return False
        if num==2:
            return True
        if num%2==0:
            return False
        for i in range(3,int(num**0.5)+1,2):
            if num%i==0:
                return False
        return True
    @staticmethod
    def factorial(n) -> int:
        if not isinstance(n,int) or n<0:
            raise ValueError("Factorial is only defined for non-negative integers.")
        if n==0 or n==1:
            return 1
        fact = 1
        for i in range(1,n+1):
            fact*=i
        return fact
print(MathUtils.is_prime(2))
print(MathUtils.is_prime(3))
print(MathUtils.is_prime(9))
print(MathUtils.is_prime(16))
print(MathUtils.factorial(5))
print(MathUtils.factorial(6))
print(MathUtils.factorial(0))
print(MathUtils.factorial(-8))


# Project Level 
  # 6. Student Grade Utility 
     # Class: GradeUtils
     # Static methods: calculate_gpa(grades), validate_grade(grade) -> ensure grade is valid(A-F)
  #  7. Inventory Utility
     # Class: InventoryUtils
     # Static method: validate_sku(sku) -> check SKU Format, calculate_discount(price,percent) -> reutrn discounted price.
     # Real use: manage shop inventory.
            