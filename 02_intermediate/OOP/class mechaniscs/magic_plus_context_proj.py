from contextlib import contextmanager
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
     # Representation
    def __str__(self):
        return f"{self.owner}'s account balance: {self.balance}$"
    def __repr__(self):
        return f"BankAccount(Owner: {self.owner}, Balance: {self.balance}$)"
    
    # Arithemetic 
    def __add__(self,amount):
        return BankAccount(self.owner,self.balance + amount)
    def __sub__(self,amount):
        if amount > self.balance:
            raise ValueError("Insufficent Fund!")
        return BankAccount(self.owner,self.balance-amount)
    
    # Comparison
    def __lt__(self,other):
        return self.balance < other.balance
    def __gt__(self,other):
        return self.balance > other.balance
    
    # Callable
    def __call__(self): # directly get balance by calling the object like a function
        return f"{self.balance}$ "
    
@contextmanager
def transaction_log(filename):
    f=open(filename,"a")
    try:
        yield f # provide the file object
    finally:
        f.close() # ensure cleanup
a=BankAccount("Nunnu",2000)
b=BankAccount("Lulli",1500)
print(a)
print(repr(a))

print(a>b)
print(a<b)
print(a-200)
print(b+200)

print(a()) # internally a.__call__()

with transaction_log("transactions.txt") as log:
    log.write(f"Withdraw from {a.owner}: -200$\n")
    log.write(f"Deposit to {b.owner}: +200$\n")
print("Transactions recorded safely!")
