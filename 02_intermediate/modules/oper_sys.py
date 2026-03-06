# "os" a python standard library module for direct interaction with the operating system.
   # used for operations:
          # path handling
          # directory traversal
          # file operations
          # metadata
          # environment variables 
          # simple process control
# Why Use "os"
   # Portability: write code that works across Windows,macOS,Linux. 
   # Automation: programmatically manage files and folders.
   # Intergration: read/set environment variables and spawn child processes.
   # Inspection: get file metadata for logging, rotation, or monitoring.
# Problems "os" solves:
   # Hardcoded path separators and platform differences.
   # Manual, error-prone shell scripting for file management
   # Discovering and processing large directory trees.
   # Needing environment configuration inside scripts. 
   # Performing atomic file operations to avoid partial writes.
# Uses and Use Cases:
   # Batch file operations: rename,move,delete many files
   # Directory scanning: find files by extension or age.
   # Safe writes: atomic replace to avoid corrupt outputs.
   # Build scripts: create artifact folders, set permissions.
   # CI and testing: create isolated temp dirs and set env vars.
   # Light process control: run commands and set enviroment fro child precesses.
# Key Concepts 
   # current working directory: os.getcwd()
   # Change directory: os.chdir(path)
   # Path joining: os.path.join(base,file)
   # Check existence: os.path.exists(path)
   # Check file vs directory: os.path.isfile(path),os.path.isdir(path)

   # List directory contents: os.listdir(path)
   # Make directories: os.mkdir(path),os.makedirs(path,exist_ok=True)
   # Remove files/directories: os.remove(file),os.rmdir(dir)
   # Rename/move files: os.rename(src,dest)

   # File metadata: os.start(path) -> size, modification time.
   # Environment variables: os. environ["PATH"], os.getenv("HOME")
   # Process control: os.system("echo Hello"), os.startfile(file)

   # Atomic opeartions: safely replace files.
   # Directory traversal: os.walk(path) for recursive scanning.
   # Permissions: os.chmod(path,mode)
   # Integration with other modules: combine os with shutil, subprocess, pathlib.

# Operating and Functioning

# Path operations and checks
import os
cwd=os.getcwd()
p=os.path.join(cwd,"data","input.csv")
if os.path.exists(p) and os.path.isfile(p):
    print("Ready: ",p)

# Challenges

# Level Beginner

# Print your current working directory
cwd=os.getcwd()
print("Current working directory: ",cwd)
# Create a path to a file called data.txt inside a folder project.
path=os.path.join(cwd,"Project","data.txt") # builds a path using the correct separator
print(path)
# Check if previous file exists.
if os.path.exists(path):
    if os.path.isfile(path):
        print("File exists:",path)
    else:
        print("Path exists but file doesn't "  , path)
else:
    print("File does not exists: ",path)
   
# Level Intermediate

# Make a folder called backup1.
os.makedirs(os.path.join(os.getcwd(),"backup1"),exist_ok=True)
# Move all .jpg file from project into backup1.
# Print confirmation for each file moved.
import shutil
dst=os.path.join(os.getcwd(),"backup1")
src=os.path.join(os.getcwd(),"project1")
os.makedirs(src,exist_ok=True)
for name in os.listdir(os.path.join(os.getcwd(),"project1")):
    if name.endswith(".jpg"):
        src_path=os.path.join(src,name)
        dst_path=os.path.join(dst,name)
        shutil.move(src_path,dst_path)
        print("Moved: ",name)



