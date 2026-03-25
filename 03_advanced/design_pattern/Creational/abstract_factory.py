"""
Abstract Factory Pattern
  -> a creational design pattern that provides an interface for creating families of related or 
     dependent objects without specifying their concrete classes.
  -> It's like a factory of factories, instead of producing just one product, it produces a set
     of products that belong together.

 Intent:
  -> To encapsulate object creation for related products.
  -> To ensure consistency among products that are meant to work together.
  -> To allow the client to switch between product families easily, without changing client code.
  
 Use Case:
  -> Cross-platform applications(e.g. GUI toolkit that create Windows buttons, Mac buttons, Linux buttons.)
  -> Multi-channel systems(e.g. Notification system that must create notifiers for WebApp vs MobileApp.)
  -> Database connectors(e.g. Factories for SQL vs NoSQL families of objects.)

"""
# Example
""" DataBase Connector(SQL vs NoSQL) """

# Abstract Products
class QueryBuilder:
    def build_query(self):
        raise NotImplementedError
class TransactionManager:
    def manage_transaction(self):
        raise NotImplementedError

# Concrete Products for SQL
class SQLQueryBuilder(QueryBuilder):
    def build_query(self):
        print("Building SQL query: SELECT * FROM users")
    
class SQLTransactionManager(TransactionManager):
    def manage_transaction(self):
        print("Managing SQL transaction")

# Concret Products for NoSQL
class NoSQLQueryBuilder(QueryBuilder):
    def build_query(self):
        print("Building NoSQL query: { find: 'users'}")

class NoSQLTransactionManager(TransactionManager):
    def manage_transaction(self):
        print("Managing NoSQL transaction")

# Abstract Factory:
class DatabaseFactory:
    def create_query_builder(self):
        raise NotImplementedError
    def create_transaction_manager(self):
        raise NotImplementedError
    
# Concrete Factories
class SQLFactory(DatabaseFactory):
    def create_query_builder(self):
        return SQLQueryBuilder()
    def create_transaction_manager(self):
        return SQLTransactionManager()
    
class NoSQLFactory(DatabaseFactory):
    def create_query_builder(self):
        return NoSQLQueryBuilder()
    def create_transaction_manager(self):
        return NoSQLTransactionManager()

# Client Code
def client_code(factory: DatabaseFactory):
    qb=factory.create_query_builder()
    tm=factory.create_transaction_manager()
    qb.build_query()
    tm.manage_transaction()

# Test with SQL
print(f"{'-'*7} SQL DataBase {'-'*7}")
client_code(SQLFactory())

# Test with NoSQL
print(f"{'-'*7} NoSQL DataBase {'-'*7}")
client_code(NoSQLFactory())
