"""
Builder Pattern
 -> a creational design pattern that helps contruct complex objects step by step.
 -> Instead of creating an object in one go iwth a huge contructor, the builder lets you assemble it gradually,
    cotrolling the construction process and final representation.

 Why it is Used:
  -> Simplifies object creation when constructors have too many parameters
  -> Improves readablity by breaking down contruction into steps.
  -> Provides flexibility to create different representations of the same object.
  -> Separates contruction logic from the object itself.
  -> Supports immutablility by building objects in a controlled way.

 Intent
   -> Separate the construction of a complex object from its representation, allowing the same construction
      process to create different representations.

 Use Case:
   -> A pratical example is in UI frameworks or document generation:
      - Building a PDF report step by step(title, table of contents, charts, footer).
      - Constructing a meal order in a food delivery app(burger, fries, drink, dessert).
      - Creating a house object with optional parts(garage, graden, swimming pool).

 Essentail Elements
    Builder Interface
     -> Defines the steps to build parts of the product.
    Concrete Builder
     -> Implement the steps to build specific representations.
    Product
     -> The final complex object being built.
    Director
     -> Controls the building process, deciding the order of steps.
    Client
     -> Requests the product through the builder.
     
"""