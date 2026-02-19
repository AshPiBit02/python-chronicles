# List = [] ordered and changeable, accepts duplicates
# usecase: storing a collection of items where order matters and add/remove is done frequently(equivalent to C++ vector)
# my_list=[] # emplty list
# my_list=[1,2,3,"apple"] # heterogeneous types allowed
# my_list=list(range(5)) # constructor form

# my_list.append(6) # push_back
# my_list.insert(0,"start") # insert at index
# my_list.extend([7,8]) # append another list
# val=my_list.pop() # remove and return last element

# sub=my_list[1:4] # elements from index 1 to 3
# rev=my_list[::-1] # reverse the list

# squares=[x**2 for x in range(1,10)] # inline transformation
# print(squares)

#Challenge 1 (basic insert/delete)
# my_list=[10,20,30,40,50]
# # 1. Add 60 to the end of the list
# my_list.append(60)
# print(my_list)
# # 2. Insert 5 at the very beginning of the list.
# my_list.insert(0,5)
# print(my_list)
# # 3. Remove the element 30 by its values.
# my_list.remove(30)
# print(my_list)
# # 4. Remove the element at index 2 and store it in a variable called removed_item
# removed_item=my_list.pop(2) # inside pop pass index or leave as it is to pop last element
# print(removed_item)
# # 5. Check if 20 exists in the list without using a loop.
# is_present=20 in my_list # returns bool and store in is_present
# print(is_present)

# if 20 in my_list:
#     print("Present")
# else:
#     print("Not present!")

# #Challenge 2 (slicing)
# numbers=[x for x in range (10)]
# # 1. Extract the first three elements using a single slice
# slice=numbers[:3]
# print(slice)
# # 2. Extract the last two elements using negative indexing
# slice=numbers[-2:]
# print(slice)
# # 3. Create a new list containing every second number(0,2,4,...)
# sec_list=[x for x in numbers[::2]]
# print(sec_list)
# # 4. Reverse the entire list using only the slicing syntax
# revnum=numbers[::-1]
# print(revnum)
# # 5. Replace the elements from index 2 to 4 with a single value[99]
# numbers[2:5]=[99]
# print(numbers)

#Challenge 3 (list comprehension)
raw_data=[x for x in range(1,11)]
print(raw_data)
# 1. Generate a new list called squares containing the squres of every number in raw_data
square_list=[x**2 for x in raw_data]
print(square_list)
# 2. Generate a list called evens that contains only the even numbers for raw_data
evens=[x for x in raw_data[1::2]]
print(evens)
# 3 . Generate a list that contains the string "Even" if the number is even and 
# "Odd " if it is odd(using a ternary operator inside the comprehension)
lables=["Even" if x%2==0 else "Odd" for x in raw_data]
print(lables)




