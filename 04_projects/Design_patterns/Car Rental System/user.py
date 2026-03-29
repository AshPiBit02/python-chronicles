from app import GPS,Insurance,ChildSeat,ExtraMileage,CarRental
hilux=CarRental("Toyota Hilux",base_price=8000,duration=3)
isuzu=CarRental("Isuzu D-max",base_price=9000,duration=2)

rent=ChildSeat(hilux)

print(f"{'-'*7} Car Rental {'-'*7}")
print(rent.description())
print('-'*25)
print(f"Total Cost: {rent.cost()}$")


rent2=GPS(Insurance(ChildSeat(isuzu)))

print(f"{'-'*7} Car Rental {'-'*7}")
print(rent2.description())
print('-'*25)
print(f"Total Cost: {rent2.cost()}$")
