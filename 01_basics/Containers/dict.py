# Dictionary
# a collection of key_value pairs
# Python 3.7+ preserve insertion order
# uses a highly optimized hash table
# use case: Fast lookups,representing JSON-like data, or mapping unique keys to values.

#initialization
my_dict={} #Empty dict if any_name{} 
print(type(my_dict))
my_dict={"name":"chdou","age":21} # standard literal 
print(my_dict)
my_dict=dict(name="Chdou",age=21) # constructor syntax
print(my_dict)

# Accessing
val=my_dict["name"] # standard access(throws keyError if missing)
print(val)
val=my_dict.get("status","default") # safe access with default value
print(val)

# Updates 
my_dict["city"]="NY" # insert/Update
my_dict.update({"age":3,"job":"IA"}) # bulk update

print(my_dict)

# Iteration
keys=my_dict.keys() # view of keys
print(keys)
values=my_dict.values() # veiw of values
print(values)
for k,v in my_dict.items(): # iterating over pairs
    print(k,v)

