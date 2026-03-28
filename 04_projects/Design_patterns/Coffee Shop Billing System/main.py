from app import BasicCoffee,ChocolateDecorator,MilkDecorator,SugarDecorator,DiscountDecorator,TaxDecorator,build_coffee,LoyaltyDecorator
# coffee=TaxDecorator(DiscountDecorator(MilkDecorator(ChocolateDecorator(BasicCoffee(size="medium"))),discount_percent=20),vat_percent=13)
total=ChocolateDecorator(MilkDecorator(SugarDecorator(BasicCoffee(size="large"))))
after_discount=DiscountDecorator(total,discount_percent=43)
after_vat=TaxDecorator(after_discount)
loyalty=LoyaltyDecorator(after_vat)
# print("Coffee Cost: $",coffee.description())
print("Order: ",total.description())
print(f"Total cost: ${total.cost()}")
print("Order: ",after_discount.description())
print(f"Total cost: ${after_discount.cost()}")
print("Order: ",after_vat.description())
print(f"Total cost: ${after_vat.cost()}")

addition=["sugar","milk","chocolate"]
coffee=build_coffee(size="large",choices=addition)
print("Order: ",coffee.description())
print(f"Total cost: ${coffee.cost()}")



print('*'*35)
print("Order: ",total.description())
print("Receipt: ")
for item,price in after_vat.receipt():
    print(f"{item}: {price}")
print('-'*15)
print(f"Total: ${after_vat.cost()}")
print(f"Loyalty Points Earned: ",loyalty.loyalty_points())


