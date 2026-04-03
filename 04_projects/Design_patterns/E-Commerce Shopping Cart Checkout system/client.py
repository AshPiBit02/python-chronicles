from app import GiftCheckoutBuilder,ExpressCheckoutBuilder,Director,StandardCheckoutBuilder

print("\n--- Standard Checkout ---")
std_builder = StandardCheckoutBuilder()
director = Director(std_builder)
std_report = director.construct(items=["Laptop", "Mouse"], discount_percentage=0.1, shipping_cost=500, payment_amount=60000, customer_name="Aashish")
std_report.show()

print("\n--- Express Checkout ---")
exp_builder = ExpressCheckoutBuilder()
director = Director(exp_builder)
exp_report = director.construct(items=["Book"], discount_percentage=0, shipping_cost=100, payment_amount=500, customer_name="Aashish")
exp_report.show()

print("\n--- Gift Checkout ---")
gift_builder = GiftCheckoutBuilder()
director = Director(gift_builder)
gift_report = director.construct(items=["Watch"], discount_percentage=0.05, shipping_cost=200, payment_amount=5000, customer_name="Aashish", gift_message="Happy Birthday!")
gift_report.show()

print("\n--- Gift Checkout ---")
gift_builder = GiftCheckoutBuilder()
director = Director(gift_builder)
gift_report = director.construct(items=["World War 3","Keyboard"], discount_percentage=0.05, shipping_cost=200, payment_amount=5000, customer_name="Aashish", gift_message="Happy Birthday!")
gift_report.show()