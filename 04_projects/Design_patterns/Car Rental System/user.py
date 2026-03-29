from app import GPS,Insurance,ChildSeat,ExtraMileage,CarRental
hilux=CarRental("Toyota Hilux",base_price=8000,duration=3)
rent=ChildSeat(hilux)
print(rent.cost())
print(rent.description())
