"""
Observer Design Pattern
 -> a design pattern where one object(called the subject) maintains a list of dependents(called observers) and 
    automatically notifies them whenever its state changes.

 Why It Is Used:
  i. Decoupling -> Separates the subject(data source) from observers(listeners), making systems modular.
  ii. Scalability -> Multiple observers can react to the same event without changing the subject's code.
  iii. Flexibility -> Observers can be added or removed at runtime.
  iv. Real-time updates -> Useful for systems that need automatic notifications when data changes.

 Intent:
  -> The intent of the Observer Pattern is "Define a one-to-many dependency so that when one object changes state, 
     all its dependents are automatically notified and updated."

 Use Case:
  A practical example is in machine learning model training dashboards:
    -> The subject is the training process.
    -> The observers are components like accuracy graphs, loss monitors, or alert systems.
    -> Whenever the training state changes(new epoch,new metric), all observers are notified and update their 
       displays automatically.

 Essential Elements:
  1. Subject(Publisher) -> Holds state and notifies observers.
  2. Observer(Subscriber) -> Reacts to updates from the subject.
  3. Concrete Subject -> Implements the subject, maintains data.
  4. Concrete Observer -> Implements the observer, defines how to react.
  5. Attach/Detach Methods -> Allow observers to subscrible/unsubscribe.
  6. Notify Method -> Send updates to all observers.

  Example: Simple Analogy
  Imagine a YouTube Channel:
    -The channel is the subject.
    -Subscribers are the observers.
    -When the channel uploads a new video, all subscribers get notified automatically.
    -The channel doesn't need to know who the subscribers are. It just broadcasts updates.

"""
# Basic Automatic notifications example using code implementation

# Subject
class Subject:
    def __init__(self):
        self._observers=[]
    def attach(self,oberver):
        self._observers.append(oberver)
    def detach(self,oberver):
        self._observers.remove(oberver)
    def notify(self,message):
        for observer in self._observers:
            observer.update(message)
    
# Observer Interface
class Observer:
    def update(self,message): pass

# Concrete Observers
class EmailSubscriber(Observer):
    def update(self, message):
        print(f"Email received: {message}")

class SMSSubscriber(Observer):
    def update(self, message):
        print(f"SMS received: {message}")

# Usage 
sub=Subject()
email=EmailSubscriber()
sms=SMSSubscriber()

sub.attach(email)
sub.attach(sms)
sub.notify("New Product Launched.")