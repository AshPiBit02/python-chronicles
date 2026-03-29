# Base Component
class CarRental:
    def __init__(self,car_model,base_price,duration=1):
        self.car_model=car_model
        self.duration=duration
        self.base_price=base_price
    def cost(self):
        return self.base_price * self.duration
    def description(self):
        return f"Car Mode: {self.car_model}\nRent Cost: {self.base_price}$\n Days: {self.duration}"
    
# Abstract Decorator
class RentalDecorator:
    def __init__(self,carRental):
        self.carRental=carRental
    def cost(self):
        return self.carRental.cost()
    def cost(self):
        return self.carRental.description()
    


    
