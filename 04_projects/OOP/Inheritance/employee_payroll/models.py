class Employee:
    def __init__(self,name,base_salary):
        self.name=name
        self.base_salary=base_salary
    def calculate_salary(self):
        """Defualt salary calculation"""
        return self.base_salary
    def __str__(self):
        return f"{self.name} earns {self.calculate_salary()}$ per month"
class FullTimeEmployee(Employee):
    def __init__(self,name,base,base_salary,bonus=0)