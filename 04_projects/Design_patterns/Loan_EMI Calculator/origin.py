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

# Common EMI Calculator logic
def calculate_emi(principle,annual_rate,years):
        R = annual_rate/12/100
        N = years*12
        emi=(principle* R * math.pow(1 + R,N))/(math.pow(1 + R, N)-1) #  emi formula
        total_payment=emi*N
        total_interest=total_payment - principle
        return emi,total_payment,total_interest

# Concrete Builder
class EMILoanBuilder(LoanBuilder):
     def __init__(self):
          self.report=LoanReport()
     def set_principle(self, amount):
          self.report.principle=amount
     def set_interest_rate(self, rate):
          self.report.annual_rate=rate
     def set_duration(self, years):
          self.report.duration_years=years
     def calculate_emi(self):
          emi,total_payment,total_interest=calculate_emi(self.report.principle,
                                                              self.report.annual_rate,self.report.duration_years)
          self.report.emi=emi
          self.report.total_payment=total_payment
          self.report.total_interest=total_interest
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
    
