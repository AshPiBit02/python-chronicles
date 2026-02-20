# # Dictionary
# # a collection of key_value pairs
# # equivalent to unordered_map (in c++)
# # Python 3.7+ preserve insertion order
# # uses a highly optimized hash table
# # use case: Fast lookups,representing JSON-like data, or mapping unique keys to values.

# #initialization
# my_dict={} #Empty dict if any_name{} 
# print(type(my_dict))
# my_dict={"name":"chdou","age":21} # standard literal 
# print(my_dict)
# my_dict=dict(name="Chdou",age=21) # constructor syntax
# print(my_dict)

# # Accessing
# val=my_dict["name"] # standard access(throws keyError if missing)
# print(val)
# val=my_dict.get("status","default") # safe access with default value
# print(val)

# # Updates 
# my_dict["city"]="NY" # insert/Update
# my_dict.update({"age":3,"job":"IA"}) # bulk update

# print(my_dict)

# # Iteration
# keys=my_dict.keys() # view of keys
# print(keys)
# values=my_dict.values() # veiw of values
# print(values)
# for k,v in my_dict.items(): # iterating over pairs
#     print(k,v)

# Challenge 1 (baiscs)
my_dict={"name":"ALice","age":"25","is_admin":"True"}
# 1. Access the "name" value
val=my_dict["name"]
print(val)
# 2. Update the "age" to 26
my_dict["age"]=26
print(my_dict)
# 3. Add a new key-value pair: "email":"alice@gmail.com"
my_dict.update({"email":"alice@gmail.com"})
print(my_dict)
for k,v in my_dict.items():
    print(k,v)
# 4. Use the .get() method to look for a key called "phone".
val=my_dict.get("phone","not found!") # if we try to access a key that is no present in list it will return the default value
                                      # but we use my_dict["phone"] it will generate error as phone is not present so, .get() method is safe
print(val)

# Challenge 2 (Iteration)
# 1. Loop through the dictionary and print only the keys
print("Keys")
for k,v in my_dict.items():
    print(k)
# 2. Loop through and print only the values.
print("Values")
for k,v in my_dict.items():
    print(v)
# 3. Loop through and print both key and values at the same time
print("Keys : Values")
for k,v in my_dict.items():
    print(f"{k} : {v}")

# Challenge 3 (Dictionary Comprehension)
number=[1,2,3,4,5]
# Use a comprehension to create a dictionary where the key is the number and the values is its squares
square_dict={x:x**2 for x in number} 
print(square_dict)


