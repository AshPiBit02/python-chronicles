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

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

