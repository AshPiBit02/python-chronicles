"""
Factory Pattern 

A creational design pattern that creates objects without exposing the exact class used.
Instead of directly instantiating classes, you:
   i. Ask a factory to create the object.
   ii. The factory decides which class to instantiate.
  
Why it is used:
  Without factory:
     i. code has many: if-else/switch
     ii. Tight coupling to specific classes
     iii. Hard to extend
  With factory:
     i. Centralized object creation 
     ii. Easy to add new types
     iii. Cleaner and scalable code
 core idea -> create objects indirectly to reduce dependency.

Intent:
  -> Provide an interface for creating objects,but let the system decide which class to instantiate.

"""

"""
Essential Elements:
  1. Product(Base Interface)
     common structure
      class Model:
          def train(self):
              pass

  2. Concrete Products(actual implementations)
      class SVM(Model):
          def train(self):
              print("SVM")
      class RandomForest(Model):
          def train(self):
              print("RF")

  3. Factory(creates objects)
      class ModelFactory:
          def get_model(self,name):
              pass

  4. Client
     -> uses factory(does NOT create objects directly)
         
"""

# Example

# Define Product Interface
class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclasses must implement drive()")
    
# Concrete Products
class Car(Vehicle):
    def drive(self):
        return "Driving a car..."
    
class Bike(Vehicle):
    def drive(self):
        return "Riding a bike.."

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck..."

# Factory
class VechicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type=="car":
            return Car()
        elif vehicle_type=="bike":
            return Bike()
        elif vehicle_type=="truck":
            return Truck()
        else:
            raise ValueError("Unknown vechicle type")

# Client
factory=VechicleFactory()
v1=factory.get_vehicle("car")
v2=factory.get_vehicle("bike")

print(v1.drive())
print(v2.drive())