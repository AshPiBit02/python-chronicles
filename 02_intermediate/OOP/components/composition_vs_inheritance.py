# Composition Vs Inheritance
"""
Intro: 
      Inheritance -> "is-a" relationship. A subclass extends a parent class.
      Composition -> "has-a" relationship. A class contains other classes as attributes.

Why used: 
      Inheritance -> reuse behavior, polymorphism.
      Composition -> flexibility, avoids deep hierarchies, easier to change parts.

Probelm they solve:
      Inheritance -> solves code reuse but can lead to rigid hierarchies.
      Composition -> solves adaptability by combining behaviors at runtime.
    
Where are they used:
      Inheritance -> frameworks, GUI hierarchies, OOP baiscs.
      Composition -> modern design, dependency injection, game engines.

"""

# Examples for illustrating the differences

"""Inheritance(Rigid hierarchy)"""
class Animal:
    def speak(self):
        print("Generic Sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")
class GuardDog(Dog):
    def guard(self):
        print("Gurading the house")
class PetDog(Dog):
    def paly(self):
        print("Playing fetch")

"""
Here we have a deep hierarchy: Animal -> Dog -> GuardDog/PetDog.
if later we want a GuardCat, we'd need another chin (Animal -> Cat -> GuardCat)
This quickly beocmes rigid and repetitive.
"""

"""Composition(Flexible, Adaptable)"""
class Engine:
    def start(self):
        print("Engine started")
class MusicSystem:
    def play(self):
        print("Playing music")
class Car:
    def __init__(self):
        self.engine=Engine()
        self.music=MusicSystem()
    def drive(self):
        self.engine.start()
        print("Car drives")
    def entertainment(self):
        self.music.play()
car=Car()
car.drive()
car.entertainment()
# If I want another object that uses other class parts
class Truck:
    def __init__(self):
        self.engine=Engine()
        self.music=MusicSystem()
    def start(self):
        self.engine.start()
        print("Truck drives with heavy loads")
    def entertainment(self):
        self.music.play()
truck=Truck()
truck.start()
truck.entertainment()

"""
    Analogy

Inheritance is like a family tree -> once you're born into it, you can't change your lineage. 
    If you want a new trait, you must extend the tree further.

Composition is like building with LEGO blocks -> you can combine different pieces to make new
     creations without rewriting the whole structure.
"""
