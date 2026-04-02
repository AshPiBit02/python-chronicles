# Product
class ConstructionReport:
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

# Builder Interface
class ConstructionBuilder:
    def set_area(self,area): pass
    def add_materials(self,cost_per_unit): pass
    def add_labor(self,workers,wage,days): pass
    def add_equipment(self,cost): pass
    def apply_tax(self,rate): pass
    def get_result(self): pass

# Concrete Builders
class ResidentalBuilding(ConstructionBuilder):
    def __init__(self):
        self.report=ConstructionReport()
    def set_area(self,area):
        self.report.area=area
    def add_materials(self, cost_per_unit):
        self.report.material_cost=self.report.area * cost_per_unit
    def add_labor(self, workers, wage, days):
        self.report.labor_cost=workers * wage *days
    def add_equipment(self, cost):
        self.report.equipment_cost=cost
    def apply_tax(self, rate):
        subtotal=self.report.material_cost + self.report.labor_cost + self.report.equipment_cost
        self.report.tax=subtotal * (rate/100)
        self.report.total_budget=subtotal + self.report.tax
    def get_result(self):
        return self.report()

class CommercialBuilding(ConstructionBuilder):
    def __init__(self):
        self.report=ConstructionReport()
    def set_area(self,area):
        self.report.area=area 
    def add_materials(self, cost_per_unit):
        # Commercial projects often use premium materials
        self.report.material_cost=self.report.area * cost_per_unit * 1.2
    def add_labor(self, workers, wage, days):
        # Higher labor cost due to skilled workers
        self.report.labor_cost=workers * wage *days *1.5
    def add_equipment(self, cost):
        self.report.equipment_cost=cost *1.3 # heavy machinary
    def apply_tax(self, rate):
        subtotal=self.report.material_cost + self.report.labor_cost + self.report.equipment_cost
        self.report.tax=subtotal * (rate/100)
        self.report.total_budget=subtotal + self.report.tax
    def get_result(self):
        return self.report()
