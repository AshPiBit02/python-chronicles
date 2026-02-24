# The "collections" module offers high-performance alternatives to python's built-in data structures.
   # useful when you need more control, efficiency, or readability in handling data.
   # commonly used in: 
        # counting items(like word frequency)
        # maintaining order while adding/removing elements
        # grouping data with default values.
        # creating lightweight objects without writing full classes.
# Key Classes and Functions in "collections"

# 1. Counter - counts occurrence of elements in an iterable.
from collections import Counter
# text="banana"
# count=Counter(text)
# print(count)
# print(count['a'])

# # 2. defaultdict - dictionary that provides a default value if a key doesn't exist.
# from collections import defaultdict
# dd=defaultdict(int) # default value = 0
# dd['apple']+=1 
# print(dd)

# text="bananana"
# dd=defaultdict(int)
# for char in text:
#     dd[char]+=1
# print(dd)

# text="missisipi"
# dd=defaultdict(int)
# for c in text:
#     dd[c]+=1
# print(dd)

# # 3. OrderedDict - remembers the order of insertion(though in Python 3.7+, normal dicts also preserve order)
# from collections import OrderedDict
# od=OrderedDict()
# od['c']=3
# od['a']=1
# od['b']=2
# print(od)

# # 4. deque - a double-ended queue for fast appends and pops from both ends.
# from collections import deque
# dq=deque([1,2,3,4,5])
# dq.appendleft(0)
# dq.append(6)
# # dq.remove(1) # removes the first occurence of a value
# dq.rotate(1) # right rotation
# dq.rotate(-1) # left rotation
# dq.extend([7,8])
# dq.extendleft([-2,-1])
# dq.insert(2,"X") # insert at index
# print(dq)
# dq=[2,3,4,2]
# print(dq.count(2))
# print(dq.index(2))
# dq=deque([1,2,3],maxlen=3) # maintain the fixed size
# dq.append(6)
# print(dq)
# dq.clear()

# 5. namedtuple - creates tuple-like objects with named fields.
from collections import namedtuple
point=namedtuple("Point",["x","y"])
p=point(10,20)
print(p.x,p.y)

# Questions

# 1. Count the frequency of each character in "AashishChaudhary"
count=Counter("AashishChaudhary")
print(count)

# 2. Use a defaultdict to group student names by their department.
from collections import defaultdict
student_by_dept=defaultdict(list)
data=[("Aashish","CS"),("Jtun","CS"),("Njo","EE"),("Btuni","ME"),("Rotun","EE")]
for nm,dp in data:
    student_by_dept[dp].append(nm)
print(student_by_dept)

# 3. make a namedtuple called Student with fields name,age,semester and create one instance
from collections import namedtuple
Student=namedtuple("student",["name","age","semester"])
s=Student("Aashish",21,"Third")
print(s.name,s.age,s.semester)

# 4. Show how OrderedDict preserves insertion order compared to a normal dict.
from collections import OrderedDict
normal_dict={}
normal_dict["apple"]=1
normal_dict["banana"]=2
normal_dict["cherry"]=3
print("Normal Dict: ",normal_dict)

ordered_dict=OrderedDict()
ordered_dict["apple"]=1
ordered_dict["banana"]=2
ordered_dict["cherry"]=3
print("Ordered Dict: ",ordered_dict)

# the real difference is that OrderedDict has methods to reorder items, while normal dicts don't
ordered_dict.move_to_end("apple")
print("After move_to_end: ",ordered_dict)
print(ordered_dict)
ordered_dict.popitem(last=False) # pops first inserted element
ordered_dict.popitem(last=True) # pops last inserted element

