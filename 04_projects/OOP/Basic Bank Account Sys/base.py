class Account:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.__balance=balance
    def deposit(self,amount):
        if not isinstance(amount,(int,float)) or (amount <= 0):
            raise ValueError("Invalid Amount!")
        self.__balance+= amount
    def withdraw(self,amount):
        if not isinstance(amount,(int,float)) or amount <= 0:
            raise ValueError("Invlaid Amount!")
        if self.__balance < amount:
            raise ValueError("Insufficient Balance!")
        self.__balance-=amount
    def get_balance(self):
        return self.__balance
class SavingAccount(Account):
    def __init__(self,account_holder,account_number,balance,interest_rate):
        super().__init__(account_holder,account_number,balance)
        if not isinstance(interest_rate,(int,float)) or self.interest_rate < 0 :
            raise ValueError("Invalid Interest Rate!")
        self.interest_rate=interest_rate

    def apply_interest(self):
        balance=self.get_balance()
        interest_amt=(self.interest_rate/100)*balance
        self.deposit(interest_amt)
class CurrentAccount(Account):
    def __init__(self,account_holder,account_number,balance,overdraft_limit=0.0):
        super().__init__(account_holder,account_number,balance)
        self.overdraft_limit=float(overdraft_limit)
    def withdraw(self, amount):
        if not isinstance(amount,(int,float)) or amount <=0:
            raise ValueError("Invalid amount!")
        current=self.get_balance()
        if amount > current + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit!")
        self.__balance-=amount
      



        

