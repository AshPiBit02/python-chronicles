class Account:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self._balance=balance
    def deposit(self,amount):
        if not isinstance(amount,(int,float)) or (amount <= 0):
            raise ValueError("Invalid Amount!")
        self.__balance+= amount
    def withdraw(self,amount):
        if not isinstance(amount,(int,float)) or amount <= 0:
            raise ValueError("Invlaid Amount!")
        if self._balance < amount:
            raise ValueError("Insufficient Balance!")
        self._balance-=amount
    def get_balance(self):
        return self._balance
    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\n Current: {self.__balance}"
class SavingAccount(Account):
    def __init__(self,account_holder,account_number,balance,interest_rate):
        super().__init__(account_holder,account_number,balance)
        if not isinstance(interest_rate,(int,float)) or interest_rate < 0 :
            raise ValueError("Invalid Interest Rate!")
        self.interest_rate=interest_rate

    def apply_interest(self):
        balance=self.get_balance()
        interest_amt=(self.interest_rate/100)*balance
        self.deposit(interest_amt)
    def __str__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\n Current: {self.get_balance()}\nInterest Rate: {self.interest_rate}"
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
        if current < amount:
            self.overdraft_limit=(current+self.overdraft_limit)-amount # deduct the amount used from overdraft
        self._balance-=amount
    def __repr__(self):
        return f"Account Holder: {self.account_holder}\nAccount Number: {self.account_number}\n Current: {self.get_balance()}\nOverdraft Limit: {self.overdraft_limit}"



        

