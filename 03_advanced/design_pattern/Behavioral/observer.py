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

"""