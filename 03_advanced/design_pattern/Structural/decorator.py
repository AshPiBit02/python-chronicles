"""
Decorator Structural Pattern
 -> a structural design pattern that lets you add responsibilities to objects dynamically without modifying their class.
 -> It's like wrapping layers around an object to extend its behavior.

  Why It's Used:
    -> Add new functionality without touching existing code.
    -> Stack multiple behaviors at runtime.
    -> Follow the Open/Closed Principle(open for extension,closed for modification)
    -> Avoid deep inheritance hierarchies.
  Intent:
    -> Provide a flexible way to extend an object's functionality by wrapping it with decorators that share the same interface.

  Essential Elements:
    Component -> defines the interface(e.g. Notifier)
    Concrete Component -> the base object(e.g. BasicNotifier).
    Decorator -> abstract wrapper that holds a reference to a component.
    Concrete Decorators -> add specifif behaviors(e.g. EmailDecorator, SMSDecorator.)

"""

# Example Code

# Component
class Notifier:
    def send(self,message):
        raise NotImplementedError
    
# Concrete component
class BasicNotifier(Notifier):
    def send(self,message):
        print("Basic Notification: ",message)
    
# Decorator
class NotifierDecorator(Notifier):
    def __init__(self,notifier):
        self.notifier=notifier
    def send(self,message):
        self.notifier.send(message)

# Concrete Decorators
class EmailDecorator(NotifierDecorator):
    def send(self,message):
        super().send(message)
        print("Also sending EMAIL: ",message)

class SMSDecorator(NotifierDecorator):
    def send(self,message):
        super().send(message)
        print("Also Sending SMS: ",message)

# Client Usage
notifier=EmailDecorator(SMSDecorator(BasicNotifier()))
notifier.send("Order #547 confirmend!")