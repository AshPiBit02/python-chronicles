# class Pen:
#     def __init__(self,color="Black",ink_level=3):
#         self.color=color
#         self.ink_level=ink_level
#     def write(self):
#         if self.ink_level==0:
#             print("Can't write(no ink left)")
#             return 
#         # writes some data
#         print("write done")
#         self.ink_level-=1
#     def refill(self,amount):
#         self.ink_level+=amount
# p=Pen()
# p.write()
# p.write()
# p.write()
# p.write()
# p.refill(2)
# p.write()