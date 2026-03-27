# Component
class Coffee:
    def cost(self):
        raise NotImplementedError
    def description(self):
        raise NotImplementedError
    
# Concrete component
class BasicCoffee(Coffee):
    def cost(self):
        return 150
    def description(self):
        return "Coffee with"
    
# Abstract Decorator
class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self.coffee=coffee
    def cost(self):
        return self.coffee.cost()
    def description(self):
        return self.coffee.description()
    
# Concrete Decorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 25
    def description(self):
        return super().description() + " Milk"
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 10
    def description(self):
        return super().description() + " Sugar"
class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost()+ 50
    def description(self):
        return super().description() + " Chocolate"
    