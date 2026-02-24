# "itertools" a standard library module fro iterator building blocks.
    # allows to create fast, memory-efficient tools for looping, counting, grouping, and generating combinations.
    # often used in data science, algorithms, and combinatorics.
# Key Functions in "itertools"

# 1. Infinite Iterators 
    # count(start=0,step=1) - infinite counting sequence.
from itertools import count
for i in count(10,2):
    if i>20: break
    print(i)
   
   # cycle(iterable) - repeats elements forever.
from itertools import cycle
c=cycle("AB")
for i in range(5):
    print(next(c))

   # repeat(object,times=None) - repeats an object
from itertools import repeat
for x in repeat("Hi",3):
    print(x)

# 2. Iterators Terminating on Shortest Input 
   # accumulate(iterable,func=operator.add) - running totals.
from itertools import accumulate
import operator
print(list(accumulate([1,2,3,4],operator.mul)))
   # chain(*iterables) - links multiple iterables together
from itertools import chain
print(list(chain([1,2],['a','b'])))
   # compress(data,selectors) - filters data by selectors.
from itertools import compress
print(list(compress("ABCDEF",[1,1,0,1,0,0j])))
   # dropwhile(predicate,iterable) - drop items untill predicate is False
from itertools import dropwhile
print(list(dropwhile(lambda x:x<5,[1,2,3,12,6,5])))
   # takewhile(predicate,iterable) - take items while pedicate is True
from itertools import takewhile
print(list(takewhile(lambda x:x%2==0,[12,24,20,11,20,24])))
   # filterfalse(predicate,iterable) - opposite fo filter
from itertools import filterfalse
print(list(filterfalse(lambda x:x>0,[1,2,3-2,-3,0])))
print(list(filterfalse(lambda x:x%2==0,range(10))))
   
# 3. Combinatoric Generators
    # product(iterable,repeat=n) - createsian product
from itertools import product
print(list(product([1,2],['a','c'])))
    # permutations(iterable,r=None) - all possible orderings
from itertools import permutations
print(list(permutations("ABC",2))) # permutations of two characters
print(list(permutations("ABC"))) # permutations of all characters
    # combinations(iterable,r) - unique subsets of length r.
from itertools import combinations
print(list(combinations("ABCD",2)))
    # combinations_with_replacement(iterable,r) - allows repeated elements.
from itertools import combinations_with_replacement
print(list(combinations_with_replacement("ABCD",2)))

