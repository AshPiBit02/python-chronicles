# Component
class Coffee:
    def cost(self):
        raise NotImplementedError
    def description(self):
        raise NotImplementedError
    
# Concrete component
class BasicCoffee(Coffee):
    def __init__(self,size="small"):
        self.size=size 

    def cost(self):
        if self.size=="small":
            return 50
        elif self.size=="medium":
            return 70
        elif self.size=="large":
            return 90
        else:
            raise ValueError("Unknown size")
    def description(self):
        return f"{self.size.capitalize()} Coffee"
       
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
    