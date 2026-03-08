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
