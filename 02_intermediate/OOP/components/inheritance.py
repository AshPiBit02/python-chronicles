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
Animal().speak()
dog=Dog()
dog.speak()

""""Using super()"""
class Vehicle:
    def __init__(self,brand):
        self.brand=brand
class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand) # call parent constructor
        self.model=model
car=Car("Toyota","Corolla")
print(car.brand,car.model)

"""Multilevel Inheritance"""
class LivingBeing:
    def breadthe(self):
        print("Breathing....")
class Animal(LivingBeing):
    def move(self):
        print("Moving...")
class Bird(Animal):
    def fly(self):
        print("Flying...")
sparrow=Bird()
sparrow.breadthe()
sparrow.move()
sparrow.fly()

"""Multiple Inheritance"""
class Flyer:
    def fly(self):
        print("Flying high!")
class Swimmer:
    def swim(self):
        print("Swimming fast!")
class Duck(Flyer,Swimmer):
    pass
duck=Duck()
duck.fly()
duck.swim()
