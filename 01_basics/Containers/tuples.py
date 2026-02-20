# # Tuples - immutable,ordered collections
# # can store heterogeneous data, allows duplicate values
# # use case: storing fixed data, returning multiple values from a function, as dictionary keys, representing records

# t=() # empty tuples
# t=(5,) # single element tuples (without comma t will be treated as integer)
# t=5, # same
# print(t)
# t=(1,2,3) # multiple elements
# t=1,2,3 # tuple packing
# print(t)
# t=tuple([1,2,3]) # using tuple() constructor
# a,b,c = (1,2,3) # tuple unpacking
# print(a,b,c)
# t=tuple("hello") # conversion from iterable
# print(t)

# # OPERATIONS 
# # 1. Indexing and Slicing
# t=(10,20,30)
# print(t[0]) # access elements by index
# print(t[-1])
# print(t[0:2]) # slicing
# print(t[::-1]) # reverse

# # 2. Concatenation & Repetition
# t1=(1,2)
# t2=(3,4)
# print(t1+t2)
# print(t1*4) # prints t1 4 times

# # 3. Membership Test
# t=(10,20,30)
# print(20 in t) 
# print(50 not in t)

# # 4. Iteration
# for item in t:
#     print(item)

# # 5. Tuple Methods
# t=(1,2,2,4,5,6,4,6)
# print(t.count(6)) # .count(x) to count x in tuple
# print(t.index(5)) # returns the first index of x

# 6. Built-in Functions applicable to Tuples
# len(t) - length of tuple
# max(t) - maximum element
# min(t) - minimum element
# sum(t) - sum of numeric elements
# sorted(t) - returns a sorted list
# tuple(iterable) - converts iterable to tuple
# any(t) - True if any element is truthy
# all(t) - True if all elements are truthy





