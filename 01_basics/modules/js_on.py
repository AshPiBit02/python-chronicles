# JavaScript Object Notation(JSON) is a lightweight format for stroing and exchanging data.
    # widely used in APIs, configuration files, and data transfer
    # json moudule allows to convert between JSON and Python objects easily
    # Use:
       # Reading/writing congig files.
       # Sending/receiving data from web APIs
       # Saving structured data(like student records) in a portable format.
# Functions in json
import json as js

# json.dumps() python to json string
data={"name":"Aashish","age":21,"semester":"Third"}
json_str=js.dumps(data)
print(data) # python's internal representation of a dictionary
print(json_str) # valid json format understandable for another system(like an API)

# json.loads() json string to python
json_str='{"name":"Aashish","age":21,"semester":"Third"}'
data=js.loads(json_str)
print(data)
print(data["name"],data["age"])

# json.dump() write json to file
with open("student.json","w") as f:
    js.dump(data,f)

# json.load() read json from file
with open("student.json","r") as f:
    loaded_data=js.load(f)
print(loaded_data)

# Pretty Printing json 
print(js.dumps(data,indent=4)) # indent make JSON human-readable, indent=4 means use 4 spaces fro each level of nesting

# Will implement this in file system

