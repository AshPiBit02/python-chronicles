"""
Strategy Pattern
 -> a behavioral design pattern that lets you define a family of algorithms, encapsulate each one, and make
    then interchangeable.
 -> Instead of hard-coding logic, you can swap strategies at runtime depending on the situation.

 Why it is Used:
   1. Flexibility
     -> Allows switching between different algorithms without changing the client code.
   2. Maintainablility 
     -> Keeps code clean by separating concerns.
   3. Extensibility 
     -> New strategies can be added without modifying existing code.
   4. Runtime Choice
     -> Users or systems can decide which strategy to use dynamically
    
 Intent:
    -> Provide a way to define a family of algorithms, encapsulate each one, and make them interchangeable
       so that client can vary its behavior independenlty of the algorithms.

 Essential Elements:
    1. Context
      -> The main class that uses a strategy
    2. Strategy Interface
      -> Defines a common method all strategies must implement.
    3. Concrete Strategies
      -> Different implementations of the algorithm.
    4. Client 
      -> Chooses which strategy to use.

 Example
   Imagine you're traveling from home to work. You can choose different strategies:
     1. Driving a car
     2. Taking a bus
     3. Riding a bike

    The 'Context' is "going to work". The Strategy is the chosen mode of transport. You can swap 
     strategies depending on traffic, weather, or cost.
"""

# Example 2

# Strategy Interface
class PaymentStrategy:
    def pay(self,amount):
        pass
    
# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount}$ using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self,amount):
        print(f"Paid {amount}$ using PayPal.")

# Context
class ShoppingCart:
    def __init__(self,payment_strategy:PaymentStrategy):
        self.payment_strategy=payment_strategy
    def checkout(self,amount):
        self.payment_strategy.pay(amount)

# Client Usage
cart1=ShoppingCart(CreditCardPayment())
cart1.checkout(211)

cart2=ShoppingCart(PayPalPayment())
cart2.checkout(21.03)