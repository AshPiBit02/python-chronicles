"""Inventory manager using property, descriptor, and dataclass"""
class PositiveValue:
    def __set_name__(self,cls,attr):
        self.attr=attr
    def __get__(self,inst,cls):
        return inst.__dict__.get(self.attr,0)
    def __set__(self,inst,val):
        if val < 0:
            raise ValueError("Invalid Value!")
        inst.__dict__[self.attr]=val
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    price: float = PositiveValue()
    quantity: int = PositiveValue()

    @property
    def total_value(self):
        return f"Total Price: {self.quantity*self.price}$"
ram=Item("LPDDR5",7400,8)
print(ram)
print(ram.total_value) # property allow to access methods like attributes
try:
    ram.price=-200
except ValueError as e:
    print("Error: ",e)

try:
    ram.quantity=3
except ValueError as e:
    print("Error: ",e)
print(ram.total_value)