# Class (A class is like a blueprint that defines what data(attributes) and behaviors(methods) an object will have.)
# Object( An object is like real instance created from the class blueprint.)

# Define a class
class class_name:
    def __init__(self,attribute1,attribute2):
        self.attribute1=attribute1 # instance variable
        self.attribute2=attribute2

    def method_name(self):
        print("This is a method")
# Create an object (instance of the class)
obj=class_name("value1","value2")
# Access attributes
print(obj.attribute1)
# Call methods
obj.method_name()