from app import BasicCoffee,ChocolateDecorator,MilkDecorator,SugarDecorator,DiscountDecorator
coffee=DiscountDecorator(MilkDecorator(ChocolateDecorator(BasicCoffee(size="medium"))),discount_percent=20)
# print("Coffee Cost: $",coffee.description())
print(f"Order: {coffee.description()} \nTotal cost: ${coffee.cost()}")
