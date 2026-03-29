# Base Component
class CarRental:
    def __init__(self,car_model,base_price,duration=1):
        self.car_model=car_model
        self.base_price=base_price
        self.duration=duration
    def cost(self):
        return self.base_price * self.duration
    def description(self):
        return f"Car Mode: {self.car_model}\nRent Cost: {self.base_price}$\nDays: {self.duration}"
    
# Abstract Decorator
class RentalDecorator(CarRental):
    def __init__(self,carRental):
        self.carRental=carRental
    def cost(self):
        return self.carRental.cost()
    def description(self):
        return self.carRental.description()

# Concrete Decorators
class GPS(RentalDecorator):
    def cost(self):
        return super().cost() + 500
    def description(self):
        return super().description() + "\nGPS Included (+500$)"
    
class Insurance(RentalDecorator):
    def cost(self):
        return super().cost() + 1000
    def description(self):
        return super().description() + "\nInsurance Included (+1000$)"
    
class ChildSeat(RentalDecorator):
    def cost(self):
        return super().cost() + 300
    def description(self):
        return super().description() + "\nChild Seat Included (+300$)"

class ExtraMileage(RentalDecorator):
    def cost(self):
        return super().cost() + 700
    def description(self):
        return super().description() + "\nExtra Mileage Included (+700$)"



    


    
