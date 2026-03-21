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

        

