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
# # 1. Work with binary files copy an image or PDF using rb and wb.
# with open("auth.webp","rb") as file:
#     data=file.read()
# with open("dummy.png","wb") as file:
#     file.write(data)
# with open("test_file.pdf","rb") as file:
#     data=file.read()
# with open("dummy.pdf","wb") as file:
#     file.write(data)
# # 2. Build a word frequency counter that reads a text file and output the top 10 most common words.
# from collections import Counter 
#    # open and read the file
# with open("sample_text.txt","r",encoding="utf-8") as file:
#     text=file.read().lower() # convert to lowercase for uniformity
#    # split text into words
# words=text.split()
#    # count word frequencies
# word_counts=Counter(words)
#    # get top 10 most common words
# top_10=word_counts.most_common(10) # returns the 10 most frequent words.
# print("Top 10 most common words: ")
#    # Display results
# for word,count in top_10:
#     print(f"{word}:{count}")
# # 3. Handle exceptions gracefully when a file doesn't exist or is locked.
# try:
#     with open("ispresent.txt","r") as f:
#         f.read()
# except FileNotFoundError:
#     print("File doesn't exists!")
# # 4. Create a program that merges multiple text files into one.
#    # List of files to merge
# files=["file1.txt","file2.txt","file3.txt"]
# output_file="merged.txt"
# with open(output_file,"w",encoding="utf-8") as res_file:
#     for fname in files:
#         with open(fname,"r",encoding="utf-8") as infile:
#         # read content and write to merged file
#          res_file.write(infile.read())
         
#          res_file.write("\n") # add a newline between files

# Phase 4 

# Read and write JSON files(e.g. save user data and load it back)
user_data={"user_id":"23C","user_name":"user1sth","user_address":"245:43:21:11"}
with open("user_data.json","w",encoding="utf-8") as user_file:
     json.dump(user_data,user_file)
with open("user_data.json","r",encoding="utf-8") as user_file:
    loaded_data=json.load(user_file)
for k,v in loaded_data.items():
    print(f"{k}:{v}")

# Process a CSV file print all rows where a certain column matches a condition
import csv
with open("learner.csv","r") as f:
    learner=csv.DictReader(f) # reads rows as dictinories
    print("Students with Grade A:")
    for row in learner:
        if row["Grade"]=="A":
            print(row["Name"],"|",row["Age"],"|",row["Grade"])

# Build a simple backup script that copies all .txt files from one folder to another.
import os
import shutil
source_folder="source_files"
backup_folder="backup_files"
os.makedirs(backup_folder,exist_ok=True) # create backup folder if it doesn't exist
for filename in os.listdir(source_folder):
    if filename.endswith(".txt"):
     src_path=os.path.join(source_folder,filename)
     dest_path=os.path.join(backup_folder,filename)
     shutil.copy(src_path,dest_path) # copy file
     print(f"Copied:{filename}")