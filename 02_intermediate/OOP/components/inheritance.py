# Inheriance allows a class(child or subclass) to reuse and extend the functionality of another class(parent or base or superclass).
  # Why it is used:
       # Avoid code duplication
       # Create hierarchical relationships
       # Enable ploymorphism
  # Where it is used:
       # Large projects with related entities 
       # Frameworks and libraries
  # When it is used:
       # When multiple class share common attributes/methods.
       # WHen you want to extend or specialize behavior without rewritting everything.
  # Essential elements of inheritance
      # Base(Parent) class -> defines common attributes and methods.
      # Derived(child) class -> inherits from the parent, can override or extend functionality.
      # super() function -> allows calling parent methods inside child methods.
      # Method Overriding -> child redefines a parent method.
      # Multiple inhertance -> a class inherits from more than one parent.
      # Hierarchical inheritance -> multiple children iherit from the same parent.
      # Multilevel inheritance -> a child inherits from a parent, which itself is a child of another class.
  # Examples
"""Single Inheritance"""
class Animal:
    def speak(self):
        print("This animal makes a sound.")
class Dog(Animal):
    def speak(self): # overriding
        print("Woof! Woof!")
dog=Dog()
dog.speak()
An=Animal()
Animal().speak()