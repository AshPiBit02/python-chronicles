# "pathlib" is a modern, object-oriented standard library module for filesystem paths
# It replaces many os.path operations with a clearer, cross-platfrom API using "Path" objects that behaves like strings but provide methods for common filesystem tasks.

# Why it is used: 
     # Readability: Path methods read like plain English(e.g. p.exists(),p.read_text())
     # Portability: automatically uses the correct path separators for the OS.
     # Safety: reduces common bugs from manual string manipulation of paths.
     # Convenience: combines path manipulation, file I/O, and metadata access in one API.
# Problems it solves
     # Eliminates manual os.path.join and separator errors.
     # Avoids repeated open() boilerplate for simple file reads/writes.
     # Makes recursive traversal and pattern matcing simpler(rglob,glob)
     # Provides a single object type for both path operations and file I/O.
# Use and common use cases
     # Path construction: build paths without worrying about separators.
     # File I/O: quick read/write of text and bytes.
     # Directory traversal: find files with patterns or recursively.
     # Project scaffolding: create directories and files for new projects.
     # Cross-platform scripts: scripts that run on Windows, macOS, Linux without path hacks.
