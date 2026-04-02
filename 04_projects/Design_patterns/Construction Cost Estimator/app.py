# Product
class ConstructorReport:
    def __init__(self):
        self.area=0
        self.material_cost=0
        self.labor_cost=0
        self.equipment_cost=0
        self.tax=0
        self.total_budget=0
    
    def show(self):
        print(f"{'-'*7} Construction Report {'-'*7}")
        print(f"Area: {self.area}sq meters")
        print(f"Materials: {self.material_cost}$")
        print(f"Labor: {self.labor_cost}$")
        print(f"Equipment: {self.equipment_cost}$")
        print(f"Tax: {self.tax}$")
        print(f"Total Budget: {self.total_budget}$")
