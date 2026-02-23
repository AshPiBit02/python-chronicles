# Variable-length Argument ( a feature that allows a function to receive any number of arguments)
  # 1. *args(Non-keyword arguments)
     # collect extra positional arguments into a tuple.
     # useful when you don't know how many values will be passed/
  # 2. **kwargs(Keyword arguments)
     # collects extra keyword arguments into a dictionary.
     # useful when you want flexible named parameters.

# Examples(note: if you don't return anything while calling a function python automatically returns "None" as output when you call the function inside print() to wrap this use print inside function and just call from outside )
  
#using *args
def total(*args):
    return sum(args)
print(total(1,2,3,4))

#using **kwargs
def show(**kwargs):
    for roll,name in kwargs.items():
        print(f"{roll}:{name}")
show(roll=1,name="Aashish")

# Write a dunction multiply_all(*args) that multiplies all numbers passed.
def multiply_all(*args):
    prod=1
    for num in args:
        prod*=num
    return prod
print(multiply_all(1,2,3,4))

#Write a function student_info(**kwargs) that prints studnet details.
def student_info(**kwargs):
    for i,j in kwargs.items():
        print(f"Details {i}:{j}")
student_info(Name="Aashish",roll=2,Semster="Third")

#Write a function mix(*args,**kwargs) that prints both positional and keyword arguments.
def mix(*args,**kwargs):
    for i in args:
        print(i)
    for i,j in kwargs.items():
        print(f"{i} : {j} ")
mix(1,2,3,4,name="Abdt",level="Bachelor")

# Write a function average(*args) that returns the average of numbers.
def average(*args):
    print(f"Average is {sum(args)/len(args)}")
average(1,2,3,4,5,6)

# Write a function config(**kwargs) that prints system configuration details.
def config(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
config(OS="Windows",version="15.1",RAM="32GB",CPU="Intel X3",GPU="Nvidia RTX 5090Ti")

#Write a function profile(*args,**kwargs) that prints positional arguments as hobbies and keyword arguments as personal details
def profile(*args,**kwargs):
    print("Hobbies:")
    print("-"*40)
    for i in args:
        print(i)
    print("Personal Details:")
    print("-"*40)
    for i,j in kwargs.items():
        print(f"{i}: {j}")
profile("Coding","Developing","Learning","Riding","Implementing","Thinking",Name="Aashish Chaudhary",Phone_no="9746666800",Address="Nepal",Education="Undergraduate")

#Write a function report(*args,**kwargs) that prints numbers passed in *args and metadata in **kwargs.
def report(*args,**kwargs):
    print("Report numbers:")
    print("-"*40)
    if args:
        print("Numbers: ",args)
    else:
        print("No numbers provided.")
    print("Metadata")
    print("-"*40)
    if kwargs:
        for k,v in kwargs.items():
            print(f"{k}: {v}")
    else:
        print("No meta provided.")
    print("-"*40)
report(101,102,104,author="Aashish",subject="Data Structure",semester="Thirds")      

# Write a function mix_data(*args,**kwargs) that separates positional and keyword arguments clearly.
def mix(*args,**kwargs):
    print("\nPositional Arguments:")
    print("-"*40)
    if args:
        for i in args:
            print(i)
    else:
        print("No positional arguments.")
    print("\nKeyword Arguments:")
    print("-"*40)
    if kwargs:
        for i,j in kwargs.items():
            print(f"{i}: {j}")
    else:
        print("No keyword arguments")
mix("DjBravo","Mjeik","Mujnor","Tdki",Stage="The Tokyo",Nao="Juntu",Densn="Tems")
mix(Stage="The Tokyo",Nao="Juntu",Densn="Tems")
mix("DjBravo","Mjeik","Mujnor","Tdki")

#Write a function registers(*args,**kwargs) that accepts multiple IDs as *args and user details as **kwargs.
def registers(*args,**kwargs):
    print("\n\nRegister")
    if args:
        print("User IDs:")
        print("-"*40)
        for i in args:
            print(i)
    if kwargs:
        print("\nUser details:")
        print("-"*40)
        for k,v in kwargs.items():
            print(f"{k}: {v}")
registers(102,104,103,101,501,Name="Funu",Department="Tdx",Salary="That equal")