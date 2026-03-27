# Component
class Coffee:
    def cost(self):
        raise NotImplementedError
    def description(self):
        raise NotImplementedError
    def receipt(self):
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
    def receipt(self):
        if self.size=="small":
            return [("Coffee",50)]

        elif self.size=="medium":
            return [("Coffee",70)]

        elif self.size=="large":
            return [("Coffee",90)]
       
# Abstract Decorator
class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self.coffee=coffee
    def cost(self):
        return self.coffee.cost()
    def description(self):
        return self.coffee.description()
    def receipt(self):
        return self.coffee.receipt()

class DiscountDecorator(CoffeeDecorator):
    def __init__(self,coffee,discount_percent=0):
        super().__init__(coffee)
        self.discount_percent=discount_percent

    def cost(self):
        original_cost=super().cost()
        discount_amount=original_cost*(self.discount_percent/100)
        return original_cost - discount_amount
    def description(self):
        return super().description() + f" with {self.discount_percent}% discount"
    def receipt(self):
        return super().receipt() + [("Discount",f"{self.discount_percent}%")]

class TaxDecorator(CoffeeDecorator):
    def __init__(self,coffee,vat_percent=13):
        super().__init__(coffee)
        self.vat_percent=vat_percent
    def cost(self):
        total_cost=super().cost()
        vat_amount=total_cost*(self.vat_percent/100)
        return total_cost + vat_amount
    def description(self):
        return super().description() + f" including {self.vat_percent}% vat"
    def receipt(self):
        return super().receipt() + [("VAT",f"{self.vat_percent}%")]
class ReceptDecorator(CoffeeDecorator):
    def description(self):
        return f"Base coffee: {super().cost()}\n"
# Concrete Decorator
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 25
    def description(self):
        return super().description() + " Milk"
    def receipt(self):
        return super().receipt() + [("Milk",20)]
    
class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 10
    def description(self):
        return super().description() + " Sugar"
    def receipt(self):
        return super().receipt() + [("Sugar",10)]
    def receipt(self):
        return super().receipt() + [("Sugar",10)]
class ChocolateDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 50
    def description(self):
        return super().description() + " Chocolate"
    def receipt(self):
        return super().receipt() + [("Chocolate",50)]
    

def build_coffee(size,choices):
    coffee=BasicCoffee(size=size)
    for choice in choices:
        if choice=="milk":
            coffee=MilkDecorator(coffee)
        elif choice=="sugar":
            coffee=SugarDecorator(coffee)
        elif choice=="chocolate":
            coffee=ChocolateDecorator(coffee)
    return coffee
    