from app import BasicCoffee,ChocolateDecorator,MilkDecorator,SugarDecorator
coffee=SugarDecorator(MilkDecorator(ChocolateDecorator(BasicCoffee())))
# print("Coffee Cost: $",coffee.description())
print(f"Order: {coffee.description()} \n Cost: ${coffee.cost()}")
