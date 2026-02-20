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
# print(t.index(5)) # returns the first occurence index of x

# # 6. Built-in Functions applicable to Tuples
# # len(t) - length of tuple
# # max(t) - maximum element
# # min(t) - minimum element
# # sum(t) - sum of numeric elements
# # sorted(t) - returns a sorted list
# # tuple(iterable) - converts iterable to tuple
# # any(t) - True if any element is truthy
# # all(t) - True if all elements are truthy

# # Topic-wise questions and solutions

# # 1. Basic
# # create an empty tuple and a tuple with one element
# tup1=() 
# tup2=(1,)
# # Pack and unpack a tuple with 4 values.
# tup1=10,20,30 # packing
# a,b,c=tup1 # unpacking
# print(tup1)
# # convert a list [10,20,30] into a tuple
# new_tup=tuple([10,20,30])
# print(type(new_tup))

# # 2. Indexing & Slicing
# t=(10,20,30,40,50)
# # Access first element
# print(t[0])
# # Access last element
# print(t[-1])
# # Access element from index 1 to 3
# print(t[1:4])
# # Reverse the tuple using slicing
# print(t[::-1])

# # 3. Tuple Opeartions
# # Concatenate(1,2,3) and(4,5,6)
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2)
# # Repeat(7,8) three times
# t3=(7,8)
# print(t3*3)
# # Check if 20 exists in (10,20,30)
# print(20 in (10,20,30))

# # 4. Nested Tuples
# t=(1,(2,3),(4,5))
# # Access the element 3
# print(t[1][1])
# # Access the tuple (4,5)
# print(t[2])

# # 5. Tuple Methods
# # Use .count() and .index() on t=(1,2,2,3,4,2)
# t=(1,2,2,3,4,2)
# print(t.count(2))
# print(t.index(4))
# # Find the index of first occurence of 2.
# print(t.index(2))




















