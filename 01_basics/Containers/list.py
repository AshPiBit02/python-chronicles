# List = [] ordered and changeable, accepts duplicates
# usecase: storing a collection of items where order matters and add/remove is done frequently(equivalent to C++ vector)
my_list=[] # emplty list
my_list=[1,2,3,"apple"] # heterogeneous types allowed
my_list=list(range(5)) # constructor form

my_list.append(6) # push_back
my_list.insert(0,"start") # insert at index
my_list.extend([7,8]) # append another list
val=my_list.pop() # remove and return last element

sub=my_list[1:4] # elements from index 1 to 3
rev=my_list[::-1] # reverse the list

squares=[x**2 for x in range(1,10)] # inline transformation
print(squares)

