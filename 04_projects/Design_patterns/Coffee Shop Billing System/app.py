# Component
class Coffee:
    def cost(self):
        raise NotImplementedError
    
# Concrete component
class BasicCoffee(Coffee):
    def cost(self):
        return 150
    
# Abstract Decorator
class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self.coffee=coffee
    def cost(self):
        return self.coffee.cost()
    
# Concrete Decorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 25
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 10
class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost()+ 50
    
coffee=ChocolateDecorator(BasicCoffee())
# print(coffee.cost())