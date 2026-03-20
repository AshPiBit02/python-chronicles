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
    def __init__(self,name,base_salary,bonus=0):
        super().__init__(name,base_salary)
        self.bonus=bonus
    def calculate_salary(self):
        """Full-time employees get base + bonus"""
        return super().calculate_salary() + self.bonus
class PartTimeEmployee(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        """Part-time employees don't use base_salary"""
        super().__init__(name,base_salary=0)
        self.hourly_rate=hourly_rate
        self.hours_worked=hours_worked
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
