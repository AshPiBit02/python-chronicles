# Lambda Function (a small, anonymous function)
     # defined using the keyword "lamda" instead of "def"
     # can take multiple arguments but only one expresion.
     # result of that expression is automatically returned.
     # Syntax: lamda arguments: expression 
               # arguments - inputs to the function
               # expression - the single operation performed.
# Examples:

#basic example
square= lambda x: x**2
print(square(5))

#multiple arguments
add = lambda a,b:a+b
print(add(2,3))

#with map()
numbers=[1,2,3,4]
square=list(map(lambda x:x**2,numbers))
print(square)

#with filter()
number=[1,2,3,4,5,6,7,8]
evens=list(filter(lambda x:x%2==0,number))
print(evens)

#with sorted()
students=[("Aash",21),("Ross",18),("Can",2)]
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)

# When to Use Lambda
    # when you need a quick, one-function
    # when passing a function as an argument(map,filter,sorted)
    # when you don't want to clutter your code with extra def functions.

# Write a lambda function to cube a number
cube=lambda x:x**3
print(f"The cube is {cube(2)}")

# Use a lambda with map() to double each number in [1,2,3,4,5]
numbers=[1,2,3,4,5]
double=list(map(lambda x:x*2,numbers))
print(double)

# Use a lambda with filter() to get numbers greater than 10 from [5,12,18,7,3]
number=[5,12,18,7,3]
result=list(filter(lambda x:x>10,number))
print(result)

# Write a lambda that checks if a string starts with "A"
start_with_A=lambda s:s.startswith("A") # .startswith() is a build-in function
print(start_with_A("Aashish"))
print(start_with_A("Tudin"))
 
# Use a lambda with filter() to select words longer than 5 characters from ["apple","banana","kiwi","strawberry"]
fruits= ["apple","banana","kiwi","strawberry"]
fruits_with_ch_gr5=list(filter(lambda s:len(s)>5,fruits))
print(fruits_with_ch_gr5)

import functools as ft
#Use a lambda with reduce() to find the product of numbers [1,2,3,4]
num=[1,2,3,4]
prod=ft.reduce(lambda x,y:x*y,num) # x=1,y=2 then x*y=2  ;  x=2,y=3 then x*y=6  ;  x=6,y=4 then x*y=24
print(prod)

# Use a lambda with reduce() to concatenate a list of strings["Hello","World","Python"]
str=["Hello","World","Python"]
str_cnc=ft.reduce(lambda x,y:x+y,str)
print(str_cnc)

# Write a lambda that returns True if a number is divisible by both 3 and 5
result=lambda x: x%3==0 and x%5==0
print(result(15))

# Write a lambda that reverse a string
rev_str=lambda x: x[::-1]
print(rev_str("Wavin Flag"))

# Use a lambda with map() to add 10 to each elements in [5,15,25]
nums=[5,15,25]
add_10=list(map(lambda x : x+10 ,nums))
print(add_10)

# Use a lamda with filter() to get all names starting with "A" from ["Aashish","Bina","Anil","Kiran"]
names= ["Aashish","Bina","Anil","Kiran"]
names_with_A=list(filter(lambda x:x.startswith("A"),names))
print(names_with_A)