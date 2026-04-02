from app import ResidentalBuilding,Director,CommercialBuilding,RoadProjectBuilder

print(f"{'-'*7} Residental Project {'-'*7}")
res_dir=Director(ResidentalBuilding())
res_report=res_dir.construct(area=200,cost_per_unit=150,workers=10,wage=50,days=30,equipment_cost=5000,tax_rate=10)
res_report.show()

print(f"{'-'*7} Commercial Project {'-'*7}")
comm_dir=Director(ResidentalBuilding())
comm_report=comm_dir.construct(area=100,cost_per_unit=200,workers=50,wage=80,days=60,equipment_cost=20000,tax_rate=15)
comm_report.show()

print(f"{'-'*7} Road Project {'-'*7}")
road_dir=Director(ResidentalBuilding())
road_report=road_dir.construct(area=500,cost_per_unit=100,workers=100,wage=60,days=90,equipment_cost=30000,tax_rate=12)
road_report.show()
