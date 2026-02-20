# A set is collection that is unordered, unindexed, and most importantly
# Contains no duplicate elements.
# it uses a hash table, making membership test O(1) significantly faster than lists (O(n))
# use case: membership testing(x in my_set), removing duplicates from a list, and mathmatical ser Opearations(union, intersection)
# Equivalent to C++ unordered_set

my_set={1,2,3,3} # duplicate removes automatically
print(my_set)
my_set=set([1,2,3,4,5,2]) # changes list in to set
print(my_set)
empty_set=set() #Note: {} inplace of set() creates an empty dict, no a set 
print(type(empty_set)) 

my_set.add(5) # insert
print(my_set)
my_set.remove(1) # remove(throws error if not found)
print(my_set)
my_set.discard(10) # Safe remove (no error if missing)

set_a={1,2,3}
set_b={3,4,5}
union=set_a | set_b # '|' performs union
print(union)
intersection = set_a & set_b
print(intersection)
difference = set_a-set_b
print(difference)
symmetric_diff=set_a^set_b

# Challenge 1 (unique & add/remove)
my_list=[1,2,2,3,4,4,4,5]
# 1. Convert my_list into a set called my_set to automatically remove duplicates
my_set = set(my_list)
print(my_set)
# 2. Add the number 6 to the set
my_set.add(6)
print(my_set)
# 3. Try to add number 3 again.
my_set.add(3) # will be internally rejected since 3 is already present
print(my_set)
# 4. Remove the number 2 from the set.
my_set.remove(3) # discards() is safe than remove()
print(my_set)
# 5. Use a method to remove an element that won't throw an error if the element doesn't exist
my_set.discard(10)
print(my_set)

# Challenge 2 (membership and Performance)
large_set={i for i in range(1000)}
# 1. Check if 500 is in the set.
is_present=500 in large_set
print(f"Present status: {is_present}") 
# 2. Why is 500 in large_set faster than 500 in large_list?
  # set uses uses a hash table(O(1)) where as but list uses vector logic and does linear search making the search O(n)

# Challenge 3 (mathematical Set Operation)
set_a= {1,2,3,4,5}
set_b={4,5,6,7,8}
# 1. Create a set of all unique element from both sets
union=set_a | set_b
print(union)
# 2. Create a set of element present in both sets
intersection=set_a & set_b
print(intersection)
# 3. Find elements in set_a that are not in set_b
difference=set_a-set_b
print(difference)
# 4. Find the elements that are in either set_a or set_b, but not both.
diff_in_both=(set_a - set_b) | (set_b-set_a)
print(diff_in_both)
sym_diff=set_a^set_b
print(sym_diff)

# Challenge 4 (set immutablility)
# 1. Try to create a set that contains a list
invalid_set={1,2,[3,4]}
print(invalid_set)
# 2. Why does this throw a typeErorr
 # because list are unhasable




