# Product
class FinancialReport:
    def __init__(self):
        self.income=0
        self.expenses=0
        self.saving=0
        self.tax=0
        self.net_income=0

    def show(self):
        print('-'*7," Financial Report ",'-'*7)
        print(f"Income: {self.income}$")
        print(f"Expenses: {self.expenses}$")
        print(f"saving: {self.saving}$")
        print(f"Tax: {self.tax}$")
        print(f"Net Income: {self.net_income}$") 

# Builder Interface
class ReportBuilder:
    def add_income(self,amount): pass
    def add_expenses(self,amount): pass
    def calculate_saving(self): pass
    def apply_tax(self,rate): pass
    def get_result(self): pass

# Concrete Builder
class MonthlyReportBuilder(ReportBuilder):
    def __init__(self):
        self.report=FinancialReport()
    
    def add_income(self,amount):
        self.report.income += amount
    def add_expenses(self, amount):
        self.report.expenses +=amount
    def calculate_saving(self):
        self.report.saving = self.report.income - self.report.expenses
    def apply_tax(self, rate):
        self.report.tax=self.report.income * (rate*0.01)
        self.report.net_income = self.report.income - self.report.tax
    def get_result(self):
        return self.report
    
# Director
class Director:
    def __init__(self,builder: ReportBuilder):
        self.builder=builder
    def construct(self,income,expenses,tax_rate):
        self.builder.add_income(income)
        self.builder.add_expenses(expenses)
        self.builder.calculate_saving()
        self.builder.apply_tax(tax_rate)
        return self.builder.get_result()
    
