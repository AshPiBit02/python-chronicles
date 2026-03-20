from abc import ABC
import math
class Shape(ABC):
    @classmethod
    def area(self):
        """Every Shape must implement this"""
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def __str__(self):
        return f"Area of Circle having radius {self.radius} units: {math.pi*self.radius:.2f} square units."

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def __str__(self):
        return f"Area of Rectangle having length({self.length}) & breadth({self.breadth}): {self.length*self.breadth:.2f} square units."
        

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def __str__(self):
        return f"Area of Triangle having base({self.base}) & height({self.height}): {self.base*self.height:.2f} square units."
        

