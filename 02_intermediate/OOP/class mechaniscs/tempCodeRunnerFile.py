nkAccount:
#     def __init__(self,balance=0):
#         self._balance=balance
#     def get_balance(self):
#         return self._balance
#     def set_balance(self,amount):
#         if amount<0:
#             raise ValueError("Invalid Amount")
#         self._balance=amount
# ac=Manul_BankAccount(500)
# print(ac.get_balance())
# ac.set_balance(1000)
# print(ac.get_balance())