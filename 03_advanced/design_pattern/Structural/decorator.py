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

# Example 2 (File Reader with Logging & Encryption)

# Component
class FileReader:
    def read(self,filename):
        raise NotImplementedError
    
# Concreate Component
class BasicFileReader(FileReader):
    def read(self,filename):
        print(f"Reading file: {filename}")
        return "file content"
    
# Abstract Decorator
class FileReaderDecorator(FileReader):
    def __init__(self,reader):
        self.reader=reader
    def read(self,filename):
        return self.reader.read(filename)
    
# Contrete Decorators
class LogingDecorator(FileReaderDecorator):
    def read(self,filename):
        print("[LOG]: About to read file")
        content=super().read(filename)
        print("[LOG]: Finished reading file")
        return content

class EncryptionDecorator(FileReaderDecorator):
    def read(self,filename):
        content=super().read(filename)
        print("[ENCRYPTION] Decrypting content...")
        return f"decrypted({content})"
    
# Client Usage
reader=EncryptionDecorator(LogingDecorator(BasicFileReader()))
data=reader.read("train_odc.txt")
print("Final content: ")