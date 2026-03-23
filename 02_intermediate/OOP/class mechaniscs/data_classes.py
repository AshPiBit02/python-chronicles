# Dataclasses
"""
Intro: 
      A decorator(@dataclass) that auto-generates __init__,__repr__,__eq__,etc.
      Ideal for classes that mainly store data.

Problem solved:
      Removes boilerplate code.
      Makes data containers concise and readable.

Where used:
      Configs, records, lightweight models.
      Anywhere you need structred data without heavy logic.
    
Alternative:
      Manual class definitions.
      Namedtuples(immutable).
      Pydantic models(validation + typing).
"""

# Examples

"""Without dataclass(manual boilerplate)"""
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def __repr__(self):
        return f"BankAccount(Owner: {self.owner}  Balance: {self.balance}$)"
    def __eq__(self,other):
        return self.balance==other.balance
ac=BankAccount("runig",500)
ac1=BankAccount("Tunig",100)
print(ac==ac1)

"""With dataclass"""
from dataclasses import dataclass

@dataclass
class NewBankAccount:
    owner:str
    balance: float=0.0
ac1=NewBankAccount("ghin",530)
print(ac1)
ac2=NewBankAccount("melbun",520)
print(ac1==ac2)