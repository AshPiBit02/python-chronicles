#  creates tuple-like objects with named fields.
from collections import namedtuple
point=namedtuple("Point",["x","y"])
p=point(10,20)
print(p.x,p.y)