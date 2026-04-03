# Product
class CheckoutReport:
    def __init__(self,items,discounts,shipping,payment,invoice):
        self.items=items
        self.discounts=discounts
        self.shipping=shipping
        self.payment=payment
        self.invoice=invoice
    
    def show(self):
        print("Checkout Report")
        print(f"{'-'*35}")
        print("Items: ",",".join(self.items))
        print(f"Discount: {self.discounts}$")
        print(f"Shipping: {self.shipping}")
        print(f"Payment: {self.payment}$")
        print(f"Invoice: {self.invoice}")

# Builder Interface
class CheckoutBuilder:
    def add_items(self): pass
    def apply_discount(self): pass
    def add_shipping(self): pass
    def add_payment(self): pass
    def add_invoice(self): pass
    
