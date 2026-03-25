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
