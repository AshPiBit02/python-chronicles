# Scope -> a fundamental concept that controls where variables are visible and usable.

# Local Scope 
     # a variable decleared inside a function is local to that function.
     # It only exists while the function runs.
     # cannot access it outside the function.
def my_func():
    x=10 # local variable
    print("Inside function: ",x)
my_func()
# print(x) # Error: x is not defined

# Global Scope
     # a variable decleared outside all functions is global
     # can be accessed anywhere in the file(unless shadowed by a local variable)
     # functions can read global variables, but to modify them, you must use the "global" keyword
y=20 # global variable
def my_func():
    print("Inside function: ",y) # can read global
my_func()
print("Outside function: ",y) # works fine

# Modifying Global Variables
   # without global, assigning inside a functoin creates a new local variable.
   # with global, you explicitly tell python to use the global one.
z=5
def change():
    global z
    z=100 # modifies global z
change()
print(z)
