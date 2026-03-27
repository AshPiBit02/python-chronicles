from app import BasicCoffee,ChocolateDecorator,MilkDecorator,SugarDecorator
coffee=SugarDecorator(MilkDecorator(ChocolateDecorator(BasicCoffee(size="medium"))))
# print("Coffee Cost: $",coffee.description())
print(f"Order: {coffee.description()} \nTotal cost: ${coffee.cost()}")
