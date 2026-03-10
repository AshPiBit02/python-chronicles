
#     def __init__(self,name):
#         self.name=name
#         print(f"Object {self.name} created")
#     def __del__(self):
#         print(f"Destructor called, object {self.name} deleted")
# d=Demo("test")
# del d # delete object explicitly

#    # File handling
# class FileHandler:
#     def __init__(self,filename):
#         self.file=open(filename,"w")
#         print("File opened")
#     def write(self,text):
#         self.file.write(text)
#     def __del__(self):
#         self.file.close()
#         print("File closed automatically")
# f=FileHandler("demo.txt")
# f.write("This is a demo file")