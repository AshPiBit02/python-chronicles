"""
Adapater Pattern
 -> a structural design pattern that allows two incompatible interfaces to work together.
 -> acts like a "translator" between classes or systems that otherwise couldn't communicate directly.

 Why It is Used:
  - Compatibility -> Connects code with mismatched interfaces.
  - Reusability -> Lets you reuse existing classes without modifying them.
  - Flexibility -> Makes systems more modular by separating adaptation logic.
  - Integration -> Useful when combining legacy code with new systems or external libraries.

 Intent: 
  -> Convert the interface of a class into another interface clients expect, so that classes with incompatible 
     interfaces can work together.

 Use Case:
  Imagine you're building a data science pipeline: 
   -> You have a library that outputs results as a NumPy array.
   -> Another visualization library expects a Python list.
   -> Instead of rewritting either library, you create an Adapter that converts NumPy arrays inot lists automatically.

 Essentail Elements:
   1. Target Interface -> The interface your client expects.
   2. Adaptee -> The existing class with an incompatible interface.
   3. Adapter -> The "translator" that converts Adaptee's interface into Target's interface.
   4. Client -> The code that uses the Target interface.
 
"""

# Basic Code Snippet

# Adaptee(incompatible interface)
class OldSystem:
    def specific_request(self):
        return "Data in old format"

# Target Interface
class NewSystemInterface:
    def request(self):
        pass

# Adapter
class Adapter(NewSystemInterface):
    def __init__(self,old_system):
        self.old_system=old_system
    def request(self):
        # Translate old interface to new
        data = self.old_system.specific_request()
        return f"Adapted: {data}"

# Client
old=OldSystem()
adapter=Adapter(old)
print(adapter.request())