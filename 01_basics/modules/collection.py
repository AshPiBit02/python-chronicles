# The "collections" module offers high-performance alternatives to python's built-in data structures.
   # useful when you need more control, efficiency, or readability in handling data.
   # commonly used in: 
        # counting items(like word frequency)
        # maintaining order while adding/removing elements
        # grouping data with default values.
        # creating lightweight objects without writing full classes.
# Key Classes and Functions in "collections"

# 1. Counter - counts occurrence of elements in an iterable.
from collections import Counter
text="banana"
count=Counter(text)
print(count)
print(count['a'])

# 2. defaultdict - dictionary that provides a default value if a key doesn't exist.
from collections import defaultdict
dd=defaultdict(int) # default value = 0
dd['apple']+=1 
print(dd)