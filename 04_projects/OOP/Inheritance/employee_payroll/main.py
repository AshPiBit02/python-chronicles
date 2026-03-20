from models import FullTimeEmployee,PartTimeEmployee
def main():
    lullu=FullTimeEmployee("Lulli",base_salary=50000,bonus=20000)
    rob=PartTimeEmployee("Rob",hourly_rate=750,hours_worked=81)
    print(lullu)
    print(rob)
if __name__=="__main__":
    main()
