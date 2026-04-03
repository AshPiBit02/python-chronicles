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
    def apply_discount(self,discount_percentage:float): pass
    def add_shipping(self,shipping_cost:float): pass
    def process_payment(self,payment_amount:float): pass
    def generate_invoice(self,customer_name:str): pass
    def get_result(self): pass

# Concrete Builders
class StandardCheckoutBuilder(CheckoutBuilder):
    def __init__(self):
        self.report=CheckoutReport()
    def add_items(self, items:list):
        self.report.items.extend(items)
    def apply_discount(self, discount_percentage: float):
        subtotal=sum([1000 for _ in self.report.items]) #asssume each item = 1000
        self.report.discounts=subtotal * discount_percentage
    def add_shipping(self, shipping_cost: float):
        self.report.shipping=shipping_cost
    def process_payment(self, payment_amount: float):
        self.report.payment_amount=payment_amount
    def generate_invoice(self, customer_name: str):
        self.report.invoice=f"Invoice fro {customer_name}: {self.report.payment} paid."
    def get_result(self):
        return self.report
    
class ExpressCheckoutBuilder(CheckoutBuilder):
    def __init__(self):
        self.report=CheckoutReport()
    def add_items(self, items:list):
        self.report.items.extend(items)
    def apply_discount(self, discount_percentage: float):
        # Express checkout skips discount
        self.report.discounts=0
    def add_shipping(self, shipping_cost: float):
        self.report.shipping=shipping_cost
    def process_payment(self, payment_amount: float):
        self.report.payment_amount=payment_amount
    def generate_invoice(self, customer_name: str):
        self.report.invoice=f"Invoice fro {customer_name}: {self.report.payment} paid."
    def get_result(self):
        return self.report

class GiftCheckoutBuilder(CheckoutBuilder):
    def __init__(self):
        self.report=CheckoutReport()
    def add_items(self, items:list):
        self.report.items.extend(items)
    def apply_discount(self, discount_percentage: float):
        subtotal=sum([2000 for _ in self.report.items]) #asssume each item = 2000
        self.report.discounts=subtotal * discount_percentage
    def add_shipping(self, shipping_cost: float):
        self.report.shipping=shipping_cost
    def process_payment(self, payment_amount: float):
        self.report.payment_amount=payment_amount
    def generate_invoice(self, customer_name: str):
        self.report.invoice=f"Invoice fro {customer_name}: {self.report.payment} paid."
    def add_gift_wrap(self,message:str):
        self.report.gift_message=message
    def get_result(self):
        return self.report
    
# Director class Director:
class Director:
    def __init__(self,builder:CheckoutBuilder):
        self.builder=builder
    def construct(self,items: list,discount_percentage:float,shipping_cost:float,payment_amount:float,customer_name:str,gift_message:str=None):
        self.builder.add_items()
        self.builder.apply_discount(discount_percentage)
        self.builder.add_shipping(shipping_cost)
        self.builder.process_payment(payment_amount)
        self.builder.generate_invoice(customer_name)
        if isinstance(self.builder,GiftCheckoutBuilder) and gift_message:
            self.builder.add_gift_wrap(gift_message)
        return self.builder.get_result()
    
        
    