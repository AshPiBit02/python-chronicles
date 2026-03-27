from app import BasicCoffee,ChocolateDecorator,MilkDecorator,SugarDecorator
coffee=ChocolateDecorator(BasicCoffee())
print("Coffee Cost: $",coffee.cost())