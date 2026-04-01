import math
# Product
class LoanReport:
    def __init__(self):
        self.principle=0
        self.annual_rate=0
        self.duration_years=0
        self.emi=0
        self.total_payment=0
        self.total_interest=0
    
    def show(self):
        print(f"{'-'}*7 Loan Report {'-'*7}")
        print(f"Principle: {self.principle}$")
        print(f"Annual Interest Rate: {self.annual_rate}%")
        print(f"Duration: {self.duration_years} year/s")
        print(f"Monthly EMI: {round(self.emi,2)}$")
        print(f"Total Payment: {round(self.total_payment,2)}$")
        print(f"Total Interest: {round(self.total_interest,2)}$")
    
# Builder Interface
class LoanBuilder:
    def set_principle(self,amount): pass
    def set_interest_rate(self,rate): pass
    def set_duration(self,years): pass
    def calculate_emi(self): pass
    def get_result(self) : pass

# Concrete Builder
class EMILoanBuilder(LoanBuilder):
    def __init__(self):
        self.report=LoanReport()
    def set_principle(self, amount):
        self.report.principle = amount
    def set_interest_rate(self, rate):
        self.report.annual_rate = rate
    def set_duration(self, years):
        self.report.duration_years = years
    def calculate_emi(self):
        P = self.report.principle
        R = self.report.annual_rate /12 /100 # monthly interest rate
        N = self.report.duration_years * 12 # duration in months

        emi=(P* R * math.pow(1 + R,N))/(math.pow(1 + R, N)-1) #  emi formula
        self.report.emi=emi
        self.report.total_payment= emi * N 
        self.report.total_interest= self.report.total_payment - P
    
    def get_result(self):
        return self.report
    
# Director 
class Director:
    def __init__(self,builder: LoanBuilder):
        self.builder=builder
    
    def construct(self,principle,rate,years):
        self.builder.set_principle(principle)
        self.builder.set_interest_rate(rate)
        self.builder.set_duration(years)
        self.builder.calculate_emi()
        return self.builder.get_result()
    
