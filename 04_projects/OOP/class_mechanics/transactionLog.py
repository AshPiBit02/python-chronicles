from contextlib import contextmanager
import datetime as dt
import os
# LOG_DIR="logs"
# os.makedirs(exist_ok=True)
@contextmanager
def transaction_log(filename):
    # path=os.path.filename
    f=open(filename,"a",encoding="utf-8")
    try: 
        yield f # provide the file object
    finally:
        f.close() # ensure cleanup
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def __str__(self):
        return f"BankAccount(owner= {self.owner}, Balance: {self.balance:.2f}$)"
    def __call__(self,action="balance",amount=0,other=None):
        timestamp=dt.datetime.now().replace(microsecond=0).isoformat()

        with transaction_log("log.txt") as log:
            if action == "balance":
                log.write(f"{timestamp} | Action: Balance Inqiry | Owner: {self.owner}\n")
                return self.balance
            elif action == "deposit":
                log.write(f"{timestamp} | Action: Deposit | Amount: {amount}$ | Owner: {self.owner}\n")
                self.balance+=amount
                return BankAccount(self.owner,self.balance+amount)
            elif action== "withdraw":
                log.write(f"{timestamp} | Action: Withdraw | Amount: {amount}$ | Owner: {self.owner}\n")
                self.balance-=amount
                return BankAccount(self.owner,self.balance)
            else: 
                log.write(f"{timestamp} | Action: Unknown | Owner: {self.owner}\n")
                return None
        
ac=BankAccount("Corporate1",500)
print(ac)
print(ac())
print(ac("deposit",500))
print(ac("withdraw",750))