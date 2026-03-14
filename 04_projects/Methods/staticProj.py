"""Hands-On projects using static method"""
# Level 1 
  # 1. Expense Tracker
     # Class: Expense
     # Static method: validate_amount(amount) -> ensures amount > 0
     # Instance: stores category, amount, date.
     # Real use: track daily spending safely.
  # 2. Temperature Converter
     # Class: Temperature
     # static method: c_to_f(celsius), f_to_c(fahrenheit)

# Level 2
  # 3. Email Utitlity
     # Class: EmailHelper
     # static method: validate_email(email) -> checks format with regex, mask_email(email) -> hides part of the address of privacy.
     # Real use: safe handling of user emails.
  # 4. Password Checker
     # Class: PasswordUtils
     # Staic methods: is_strong(password) -> checks length,digits,uppercase, symbols, hash_password(password) -> returns a hased version.
     # Real use: secure user authentication.

# Level 3
  # 5. File Utility
     # Class: FileUtils
     # Static methods: get_extension(filename), is_valid_filename(filename)
     # Real use: validate and process uploaded files.
  # 6. Math Helper
     # Class: MathUtils
     # Static Methods: is_prime(n), factorial(n)
     # Real use: reusable math utilities in apps.

# Project Level 
  # 6. Student Grade Utility 
     # Class: GradeUtils
     # Static methods: calculate_gpa(grades), validate_grade(grade) -> ensure grade is valid(A-F)
  #  7. Inventory Utility
     # Class: InventoryUtils
     # Static method: validate_sku(sku) -> check SKU Format, calculate_discount(price,percent) -> reutrn discounted price.
     # Real use: manage shop inventory.
            