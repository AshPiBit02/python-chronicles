"""Magic Methods(Dunder methods)"""
  # start and ends with __
  # special methods that allows objects interact with built-in Python behavior
  # Use:
    # make custom classes behave like built-in types.
    # allow operator overloading(+,-,*,etc)
    # give control over object representation(print,repr)
    # integrate with Python's built-in functions(len(),iter(),in)
"""Key Elements"""
"""
1. __init__ -> object creation
2. __del__ -> cleanup
3. __str__ -> Human-readable output format
4. __repr__ -> developer friendly string output

    compares with objects
5. __eq__ -> equals
6. __lt__ -> less than
7. __gt__ -> greater than
8. __le__ -> less than or equals
9. __ge__ -> greater than or equals
10. __ne__ -> not equals

   Operator overloading
11. __add__ 
12. __sub__
13. __mul__
14. __truediv__

   Make objects act like lists/dicts
15. __len__ -> length of obj 
16. __getitem__ -> gets item from obj
17. __setitem__ -> 
18. __delitem__ -> 
19. __contains__ -> 
 
   Support loops (for x in obj)
20. __iter__ 
21. __next__

    Makes objects behave like functions
22. __call__ 
"""

class MagicDemo:
    def __init__(self,name,values): # initialization
        self.name=name
        self.values=list(values)
    def __del__(self): # cleanup message(runs when object is deleted)
        print(f"{self.name} object is being destroyed")
    
    # Representation
    def __str__(self):
        return f"MagicDemo({self.name}) with values {self.values}"
    def __repr__(self):
        return f"MagicDemo(name={self.name!r},values={self.values!r})" # !r -> keep values inside single quote
    
    # Comparison
    def __eq__(self,other):
        return sum(self.values)==sum(other.values)
    def __ne__(self,other):
        return sum(self.values)!=sum(other.values)
    def __lt__(self,other):
        return sum(self.values)<sum(other.values)
    def __gt__(self,other):
        return sum(self.values)>sum(other.values)
    def __le__(self,other):
        return sum(self.values)<=sum(other.values)
    def __ge__(self,other):
        return sum(self.values)>=sum(other.values)
    
    # Arithemtic(operator overloading)
    def __add__(self,other):
        return MagicDemo(self.name + "+" + other.name,self.values + other.values)
    def __sub__(self,other):
        return MagicDemo(self.name + "-" + other.name,[sum(self.values) - sum(other.values)])
    def __mul__(self,other):
        new_list=[]
        for i,j in zip(self.values,other.values):
            new_list.append(i*j)
        return MagicDemo(self.name + "*" + other.name,new_list)


a=MagicDemo("adf",[1,3,6])
b=MagicDemo("acd",[3,2,6])
c=a*b
print(c)
# print(a>b)
# c=a+b
# print(c)
# print(a>=b)
# m=MagicDemo("fasd",[3,3,6,7])
# print(repr(m))
    

