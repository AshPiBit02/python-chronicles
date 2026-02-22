# Basic

# Write a function say_hello() that prints "Hello,world!".
def say_hello():
    print("Hello, world!")
say_hello()
# Write a function greet_user() that asks for a name using input() and prints "Hello,<name>"
def greet_user():
    name=input("Enter your name: ")
    print(f"Hello, {name}")
greet_user()

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

# Default Arguments

# Write a function welcome(name="Guest")  that prints "Welcome,<name>"
def welcome(name="Guest"):
    print(f"Welcome, {name}")
welcome()
# Write a function power(base,exp=2) that returns the base raised to the exponent(default square)
def power(base,exp=2):
    return base**exp
print(power(2,3))

# 3 Variable Arguments

# Write a function total(*args) that returns the sum of any number of inputs.
def total(*args): # *name allows passing any number of positional arguments( behaves like tupes) 
    return sum(args)
print(total(1,2,3,4))
print(total(1,2,3,4,5))
# Write a function show_info(**kwargs) that prints key-value pairs
def show_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
show_info(name="ABC",age=21)

# Recursion

# Write a recursive function factorial(n) that calculates factorial.
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(f"The factorail is {factorial(6)}")
# Write a recursive function fibonacci(n) that returns the nth Fibonacci number
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2) 
n=8
print(f"The fibonacci terms of {n} is {fibonacci(n)}")

# Higher-Order Functions

# Write a function apply_twice(func,x) that applies a function to x two times.
def apply_twice(square,x):
    return square(square(x))
def square(n):
    return n**2
print(apply_twice(square,2))
# Use map() with a lambda to sqaure numbers in [1,2,3,4]
numbers=[1,2,3,4]
squared=list(map(lambda n:n**2,numbers))
print(squared)



    