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