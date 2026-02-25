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
