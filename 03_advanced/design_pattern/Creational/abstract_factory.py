"""
Abstract Factory Pattern
  -> a creational design pattern that provides an interface for creating families of related or 
     dependent objects without specifying their concrete classes.
  -> It's like a factory of factories, instead of producing just one product, it produces a set
     of products that belong together.

 Intent:
  -> To encapsulate object creation for related products.
  -> To ensure consistency among products that are meant to work together.
  -> To allow the client to switch between product families easily, without changing client code.
  
 Use Case:
  -> Cross-platform applications(e.g. GUI toolkit that create Windows buttons, Mac buttons, Linux buttons.)
  -> Multi-channel systems(e.g. Notification system that must create notifiers for WebApp vs MobileApp.)
  -> Database connectors(e.g. Factories for SQL vs NoSQL families of objects.)

"""