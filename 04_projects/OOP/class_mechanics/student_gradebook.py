"""Student Gradebook using dataclass, descriptor, and property"""

from dataclasses import dataclass

class validValue:
    def __set_name__(self,cls,attr):
        self.attr=attr
    def __set__(self,inst,val):
        if val < 0:
            raise ValueError(f"Invalid value! {self.attr} must be positive")
        inst.__dict__[self.attr]=val
    def __get__(self,inst,cls):
        return inst.__dict__.get(self.attr,0)
class validRange:
    def __set_name__(self,cls,attr):
        self.attr=attr
    def __set__(self,inst,val):
        if val < 0 or val > 100 :
            raise ValueError(f"Invalid value! {self.attr} must be in range 0 - 100")
        inst.__dict__[self.attr]=val
    def __get__(self,inst,cls):
        return inst.__dict__.get(self.attr,0.0)
    
@dataclass
class Student:
    name: str
    roll_no:int =validValue()
    grade: float=validRange()
    @property
    def status(self):
        return "Pass" if self.grade >= 40 else "Fail"
stu=Student("Tungin",33,79)
print(stu.status)
# stu.grade=-29
print(stu.status)
print(stu.roll_no)
stu.roll_no=10
print(stu.roll_no)

print(stu)