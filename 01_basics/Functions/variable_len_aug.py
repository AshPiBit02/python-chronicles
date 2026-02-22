# Variable-length Argument ( a feature that allows a function to receive any number of arguments)
  # 1. *args(Non-keyword arguments)
     # collect extra positional arguments into a tuple.
     # useful when you don't know how many values will be passed/
  # 2. **kwargs(Keyword arguments)
     # collects extra keyword arguments into a dictionary.
     # useful when you want flexible named parameters.

# Examples
  
#using *args
def total(*args):
    return sum(args)
print(total(1,2,3,4))

#using **kwargs
def show(**kwargs):
    for roll,name in kwargs.items():
        print(f"{roll}:{name}")
print(show(roll=1,name="Aashish"))