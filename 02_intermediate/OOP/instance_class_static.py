# Instance 
   # These methods are functions defined inside a class whose first parameter is conventionally named 'self'.
   # When you call the method on an object, 'self' refers to that specific instance, giving the method access to the instance's attributes and other methods.
   # Uses:
        # Model object behavior: implement actions that depend on an object's state(e.g. 'account.deposit').
        # Read and update instance attributes: change 'self.balance','self.status', etc.
        # Coordinate multiple attributes: compute values derived from several instance fields.
        # Encapsulate logic: keep related behavior inside the class for clarity and reuse.
   # Key Elements:
      # Method signature: first parameter must be 'self'(or another name, but self is standard)
      # Defined insided class body: indented under class.
      # Called on instances: 'obj.method(...)' - python binds 'obj' to 'self'.
      # Can access 'self' attributes and other instance methods.
      # Can return values or mutate the instance.
