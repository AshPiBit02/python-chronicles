# # Basic

# # Write a function say_hello() that prints "Hello,world!".
# def say_hello():
#     print("Hello, world!")
# say_hello()
# # Write a function greet_user() that asks for a name using input() and prints "Hello,<name>"
# def greet_user():
#     name=input("Enter your name: ")
#     print(f"Hello, {name}")
# greet_user()

# Parameter and Return 

# Write a function add_number(a,b) that retuns that sum of two numbers
def add_number(a,b):
    return a+b;
print(add_number(8,2))
# Write a function is_even(n) that returns True if the number is even, otherwise False
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(11))