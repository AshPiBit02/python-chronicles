# "random" (generating random numbers, choice and shuffling)
     # very hardy for simulations, games, testing, and data sampling.

# Core function in random
import random as rdm

# Random float(0.0<=x<1.0)
print(rdm.random())

# Random integer in a range
print(rdm.randint(1,10)) # inclusive of both ends

# Random Choice from a list
fruits=["apple","banana","cherry","Orange","Mango"]
print(rdm.choice(fruits))

# Random Sample(Unique Picks)
numbers=[1,2,3,3,3,4,5]
print(rdm.sample(numbers,3)) # picks 3 random values 

# Shuffle a List
cards=["A","K","Q","J"]
rdm.shuffle(cards)
print(cards)

# Uniform Distribution
print(rdm.uniform(1,5)) # float between 1 and 5

# Seed(Reproducible Randomness)
# rdm.seed(42) # not fully random but calculated is generated based on seed value
print(rdm.randint(1,10))

# number guessing game
print("Number Guessing Game")
print("-"*35)
num=rdm.randint(1,100)
in_num=int(input("Guess the number: "))
count=0
while(in_num!=num):
    if(in_num>num):
        print("Input is High!")
    elif (in_num<num):
        print("Input is Low!")
    in_num=int(input("Enter next Guess: "))
    count+=1
print(f"Correct guess in {count} try")


    



