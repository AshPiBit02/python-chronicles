# Regular Expression(re/regex) are patterns used to match strings
# The "re" module allows to search, validate, and manipulate text using these patterns.
# Commonly used in:
     # Input validation(emails,phone numbers,etc)
     # Searching text(find all numbers,words,or specific formats)
     # Replacing or cleaning data(remove special characters)
# Useful Regex Patterns
   # \d -> digit(0-9)
   # \w -> word characters(letters,digits,underscore)
   # \s -> whitespace 
   # .  -> any character except newline
   # ^  -> start of string
   # $  -> end of string
   # +  -> one or more
   # *  -> zero or more
   # {n} -> exactly n times

# Functions in re
import re

# re.match(pattern,string) - checks if the string starts with the pattern
print(re.match(r"Hell","Hello World"))

# re.search(pattern,string) - finds the first occurrence of the patttern anywhere in the string.
print(re.search(r"orl","Hello world"))

# re.findall(pattern,string) - returns all matched as a list
text="Roll numbers: 101, 102, 103"
print(re.findall(r"\d+",text)) 

# re.sub(pattern,replacement,string) - replaces all matches with something else.
text="Hello 123 World 456"
print(re.sub(r"\d+","#",text))
print(re.sub(r"\d{1}","*",text))

# re.split(pattern,string) - splits a string by the regex pattern.
text="apple,banana cherry,orange"
print(re.split(r"[;, ]",text)) # [;, ] -> split when ";" or "," or " "
print(re.split(r"[a]",text)) 
num="AashishChaudharyChandrapurNepal"
print(re.split(r"[A-Z]",num))
print(re.split(r"(?=[A-Z])",num)) # lookahead(?=) -> split before any

# Questions

# Use re.findall to extract all numbers from "Students IDs: 21, 34, 56"
text="Studnents IDs: 21, 34, 56"
print(re.findall(r"\d+",text))

# Validate if a string is a proper email(basic check: contains @ and .)
email="ashpibit@gmail.com"
email1="ashpibitgmail.com"
def isvalid(email):
    if re.search(r"@" or ".",email):
        return True
    else:
        return False
print(isvalid(email1))
print(isvalid(email))

# Replace all digits in "Room 101, Floor 2 " with "X"
dimension="Room 101, Floor 2"
print(re.sub(r"\d+","X",dimension))

# Split "apple;banana,grape orange" into a list of fruits.
l_fruit="apple;banana,grape orange"
print(re.split(r"[;, ]",l_fruit))

# Search if "Nepal" exists inside "I live in Nepal and love coding".
info="I live in Nepal and love coding"
print(re.search(r"Nepal",info))

