from base import Account,SavingAccount,CurrentAccount
sa=SavingAccount("Aashish",121444490001,55000,5.7)
try:
    sa.withdraw(5000)
except ValueError as e:
    print("Error: ",e)
print(sa)
ca=CurrentAccount("Hsihsaa",233220098,2000,overdraft_limit=5000)
try:
    ca.withdraw(4000)
except ValueError as e:
    print("Error: ",e)
print(ca)