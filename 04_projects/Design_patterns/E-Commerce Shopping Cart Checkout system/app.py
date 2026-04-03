# Product
class CheckoutReport:
    def __init__(self,items,discounts,shipping,payment,invoice):
        self.items=[]
        self.discounts=0
        self.shipping=0
        self.payment=0
        self.invoice=" "
        self.gift_message=None
    
    def show(self):
        print("Checkout Report")
        print(f"{'-'*35}")
        print("Items: ",','.join(self.items))
        print(f"Discount: {self.discounts}$")
        print(f"Shipping: {self.shipping}")
        print(f"Payment: {self.payment}$")
        if self.gift_message:
            print(f"Gift Message: {self.gift_message}")
        print(f"Invoice: {self.invoice}")

# Builder Interface
class CheckoutBuilder:
    def add_items(self,items: list): pass
    def apply_discount(self,dicount_percentage:float): pass
    def add_shipping(self,shipping_cost:float): pass
    def process_payment(self,payment_amount:float): pass
    def generate_invoice(self,customer_name:str): pass
    def get_result(self): pass
    
