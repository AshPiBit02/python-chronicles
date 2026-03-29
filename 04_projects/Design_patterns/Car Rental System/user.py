from app import GPS,Insurance,ChildSeat,ExtraMileage,CarRental
hilux=CarRental("Toyota Hilux",base_price=8000,duration=3)
isuzu=CarRental("Isuzu D-max",base_price=9000,duration=2)

rent=ChildSeat(hilux)
print(rent.description())
print(f"Total Cost: {rent.cost()}$")


rent2=GPS(Insurance(ChildSeat(isuzu)))
print(rent2.description())
print(f"Total Cost: {rent2.cost()}$")
