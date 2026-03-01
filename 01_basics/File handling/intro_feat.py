# Python's file handing(open,read,write,with) is the foundation for working with persistent data.
    # beyond simpel read/write, it offeres streaming, random access, binary I/O, and safe resource management.
# Key Features

# 1. Open modes 
    # "r" -> read text
    # "w" -> wirte(overwrite)
    # "a" -> append
    # "x" -> exclusive create
    # "b" -> binary mode("rb","wb")
    # "+" -> read+write("r+","w+")     
# 2. Context manager(with)
    # ensures automatic closing of files.
    # prevents resource leaks even if errors occur.
# 3. Reading methods
    # read() -> whole file
    # readline() -> one line
    # readlines() -> list of all lines
    # iterating directly over file object -> efficient streaming
# 4. Writing methods
    # write() -> write string or bytes
    # writelines() -> write list of strings
# 5. File pointer control
    # tell() -> write string or bytes
    # seek(offset,whence) -> move pointer(start,current,end)
# 6. Binary I/O
    # read/write images,audio,or raw data with "rb"/"wb".
# 7. Atomic operations
    # write to temp file then os.replace() or Path.replace() -> avoids corruption 

# Implentations (examples)

# Read line by line(large file)
with open("big.log","r",encoding="utf-8") as f: # encodeing="utf-8" tells python how to interpret text: UTF-8 is the universal standard
    for line in f:
        print(line.strip()) # .strip() removes whitespace/newlines from start and end of a string

# Append logs
from datetime import datetime
with open("app.log","a",encoding="utf-8") as f:
    f.write(f"{datetime.now().isoformat()} - started\n") 

# Binary read/write
# Read image
with open("test.jpg","rb") as f:
    data=f.read()
# Write binary data
with open("copy.jpg","wb") as f:
    f.write(data)

# Random access
with open("data.txt","r+") as f:
    f.seek(5) # move to 5th byte
    print(f.read(10)) # read next 10 chars']

# Exception handling in file operation
try:
    with open("missing.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Please check the path.")

# Working with JSON Files
import json
data={"name":"Aashish","age":"21"}
with open("data.json","w") as f:
    json.dump(data,f)
with open("data.json","r") as f:
    loaded=json.load(f)
    print(loaded)

# # Using os and pathlib for file management
# import os 
# from pathlib import Path
# # check if file exists
# if Path("data.txt").exists():
#     print("File exits")
# # Rename file 
# os.rename("old.txt","new.txt")
# # Delete file
# os.remove("unwanted.txt")

# Challenges

#Phase 1
# 1. Create a text file and write "Hello, World!" into it.
with open("test.txt","w") as file:
    file.write("Hello, World!")
# 2. Read the file back and print its contents.
with open("test.txt","r") as file:
    print(file.read())
# 3. Append a new line to the same file without overwritting.
with open("test.txt","a") as file:
    file.write("\nWorld, Hello")
# 4. Count how many lines are in the file.
with open("test.txt","r") as f:
    lines=f.readlines() # reads all lines into a list
    print("Number of lines: ",len(lines))
  # Alternatively
count=0
with open("test.txt","r") as f:
    for line in f:
        count+=1
print("Number of lines: ",count)

#Phase 2
# 1. Read a file line by line and print only lines longer than 20 characters.
# with open("sample.txt","r",encoding="utf-8") as file:
#     for line in file:
#         clean_line=line.strip() # remove leading/tailing whitespace and new lines
#         if len(clean_line)>20:
#             print(clean_line)
# 2. Write a program that copies the contents of one file into another.
# with open("origin.txt","w",encoding="utf-8") as f:
#     f.write("These are the contents from origin file.")
# with open("origin.txt","r",encoding="utf-8") as f:
#     contents=f.read()
# with open("alternate.txt","w") as f:
#     f.write(contents)
# # 3. Create a log file that records the current timestamp each time the program runs.
# from datetime import datetime as dt
# with open("records.log","a",encoding="utf-8") as f:
#     f.write(f"{dt.now().isoformat()} - started\n")
# # 4. Use seek() to jump to a specific byte in a file and read the next 15 characters.
# with open("test.txt","r+") as f:
#     f.seek(2)
#     print(f.read(15))

# Phase 3
# 1. Work with binary files copy an image or PDF using rb and wb.
with open("auth.webp","rb") as file:
    data=file.read()
with open("dummy.png","wb") as file:
    file.write(data)