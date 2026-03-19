# Hands-On projects using instance method

# Level 1(Attribute Basics)
   # Create a 'Pen' class with attributes 'color' and 'ink_levl'.
   # Write an instance method write(text) that reduces ink level by 1 each time it's called.
   # Add another method refill(amount) that increases ink level.
class Pen:
    def __init__(self,color="Black",ink_level=3):
        self.color=color
        self.ink_level=ink_level
    def write(self):
        if self.ink_level==0:
            print("Can't write(no ink left)")
            return 
        # writes some data
        print("write done")
        self.ink_level-=1
    def refill(self,amount):
        self.ink_level+=amount
p=Pen()
p.write()
p.write()
p.write()
p.write()
p.refill(2)
p.write()
p.write()

   # Build a 'Bottle' class with attributes 'capacity' and 'current_volume'.
   # Add instance methods fill(amount) and drink(amount) to adjust the volume.
   # Prevent drink from going below 0 and fill from exceeding capacity.
class Bottle:
    def __init__(self,capacity=1000,current_volume=750):
        self.capacity=capacity
        self.current_volume=current_volume
    def fill(self,amount):
        if self.current_volume+amount > self.capacity:
            raise ValueError("Water overflow")
        self.current_volume+=amount
        print(f"{amount} ml water filled")
    def drink(self,amount):
        if self.current_volume-amount < 0:
            raise ValueError("Can't drink! (not enough water)")
        self.current_volume-=amount
        print(f"{amount} ml water deducted")
b=Bottle()
try: 
    b.fill(1)
except ValueError as e:
    print(f"Error: ", e)
try: 
    b.drink(751)
except ValueError as e:
    print(f"Error: ", e)
print(b.current_volume,"ml")
print(b.capacity,"ml")

# Level 2(State Management)
  # Design a Door class with attribute is_locked.
  # Add instance methods lock() and unlock().
  # Add a method status() that prints whether the door is locked or unlocked.
class Door:
    def __init__(self,is_locked=False):
        self.is_locked=is_locked
    def lock(self):
        if self.is_locked==True:
            print("Already locked")
            return
        self.is_locked=True
        print("Door locked")
    def unlock(self):
        if self.is_locked==False:
            print("Already Unlocked")
            return
        self.is_locked=False
        print("Door unlocked")
    def status(self):
        print(f"Status: {self.is_locked}")
d=Door()
d.status()
d.unlock()
d.lock()
d.lock()
  # Create a 'Phone' class with attributes 'battery' and is_on.
  # Add instance methods 'power_on()', 'power_off()', and charge(amount).
  # Ensure battery never goes above 100%.
class Phone:
    def __init__(self,battery=100):
        self.battery=battery
    def power_on(self):
        if self.battery <= 0:
            Phone.power_off()
            return
        self.battery-=10 # with each power on battery discharge by 10%
        print("Power ON")
    def power_off():
        print("Power OFF")
    def charge(self,amount):
        if self.battery+amount>100:
            print("Non real power")
            return
        self.battery+=amount
        print(f"Battery charged by {amount}%. Current battery: {self.battery}")
Phn=Phone()
Phn.charge(20)
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.power_on()
Phn.charge(67)
print(Phn.battery)

# Level 3 (Real-World modeling)
  # Make a 'Ticket' class with attributes event, price, and is_sold.
  # Add instance methods sell(buyer) and refund().
  # Add a method details() that shows ticket info and status.
class Ticket:
    def __init__(self,event,price,is_sold=False):
        self.event=event
        self.price=price
        self.is_sold=is_sold
    def sell(self,buyer):
        if self.is_sold==True:
            print("Ticket no availabe!")
            return
        self.is_sold=True
        print("Ticket sold to ",buyer," for ",self.event)
    def refund(self):
        if self.is_sold==False:
            print("Can't refund (ticket is not sold)")
            return 
        self.is_sold=False
        print("Refund successful")
    def details(self):
        print(f"Event: {self.event}\nPrice: Rs.{self.price}\nIs_sold: {self.is_sold}")
t=Ticket("Concert",5000)
t.sell("Atin")
t.refund()
t.details()

   # Build a 'Task' class with attributes 'title' and 'is_completed'.
   # Add intance methods 'mark_complete()' and 'mark_incomplete()".
   # Add a method 'summary()' that prints the task status.
class Task:
    def __init__(self,title=None,is_completed=False):
        self.title=title
        self.is_completed=is_completed
    def mark_complete(self):
        if self.is_completed==True:
            print(f"The {self.title} is alreday completed")
            return 
        self.is_completed=True
        print(f"The {self.title} is completed now.")
    def mark_incomplete(self):
        if self.is_completed==False:
            print(f"The {self.title} is alreday incomplete")
            return 
        self.is_completed=False
        print(f"The {self.title} is incomplete as of now.")
    def summary(self):
        """Return"""
        print('-'*40)
        print(f"Title: {self.title}\n is_completed: {self.is_completed}")
tsk=Task("Walking Dead")
tsk.summary()
tsk.mark_complete()
tsk.summary()
tsk.mark_incomplete()
tsk.summary()


