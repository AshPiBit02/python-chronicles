from database_conn import DatabaseConnection
class InventoryManager:
    def __init__(self):
        self.db=DatabaseConnection(db_url="mysql://localhost")
        self.items={}
    def add_item(self,name,quantity):
        self.items[name]=self.items.get(name,0)+quantity
        print(f"Added {quantity} {name}(s). Current stock: {self.items[name]}")

    def remove_item(self,name,quantity):
        if name not in self.items:
            print(f"{name} doesn't exist in inventory")

        elif self.items.get(name,0) >= quantity:
            self.items[name]-=quantity
            print(f"Removed {quantity} {name}(s). Current stock: {self.items[name]}")
        else:
            print(f"Not enough {name} in stock!")