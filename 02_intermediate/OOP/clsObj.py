# Class (A class is like a blueprint that defines what data(attributes) and behaviors(methods) an object will have.)
# Object( An object is like real instance created from the class blueprint.)

# Define a class
class class_name:
    def __init__(self,attribute1="default value 1",attribute2="default value 2"):
        self.attribute1=attribute1 # instance variable
        self.attribute2=attribute2

    def method_name(self):
        print("This is a method")
# Create an object (instance of the class)
obj=class_name("value1","value2")
obj2=class_name()
# Access attributes
print(obj.attribute1)
print(f"Values are {obj2.attribute1} and {obj2.attribute2}")
# Call methods
obj.method_name()


# Some essential elements
# 1. Constructor(__init__)
      # Special method that runs automatically when you create an object.
      # Used  to initialize attributes
# 2. Attributes
      # Variables that belong to an object.
      # Accessed with "self.attribute"
# 3. Methods
      # Functions inside a class that define behavior.
      # Always take "self" as the first parameter(represents the object itself).
# 4. Keywords
      # class -> defines a class.
      # self -> refers to the current object.
      # __init__ -> constructor method.
      # object.method() -> calling a method on an object
# Example
class Car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color

    def drive(self):
            print(f"The {self.color} {self.brand} is driving!")
# Create objects
car1=Car("BMW","Black")
car2=Car("Toyota","Grey")
car1.drive()
car2.drive()

# Types of Constructors
# 1. Defualt Constructor 
    # A constructor that takes no arguments(other than self).
    # It simply initializes the object with fixed/default values.
class student:
     def __init__(self): # default constructor
          self.name="Unknown"
          self.age=0
s=student()
print(s.name,s.age)
# 2. Parameterized Constructor
    # A constructor that accepts arguments to initialize attributes dynamically.
    # Most commonly used in real projects.
class student:
     def __init__(self,name,age):
          self.name=name
          self.age=age
s=student("Aash",21)
print(f"Name: {s.name} \nAge: {s.age}")
# 3. Copy Constructor( Conceptual in Python)
   # Python doesn't have a built-in copy constructor like C++
   # But can simulate it by writing a constructor that takes another object as input.
   # creates a new object as a copy of an existing object.
class learner:
     def __init__(self,name=None,age=None,other=None):
          if other: # copy constructor
               self.name=other.name
               self.age=other.age
          else: # normal constructor
               self.name=name 
               self.age=age
# Orginal Object
s1=learner("Rita",21)

s2=learner(other=s1) # copy constructor
print(s1.name,s1.age)
print(s2.name,s2.age)