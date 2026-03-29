from app import Course,Certificate,ExtraMaterails,Mentorship,LifetimeAccess

ml=Course("Machine Learning",7000)
dl=Course("Deep Learning",11000)
ds=Course("Data Science",10000)

jon=LifetimeAccess(Mentorship(ml))
rob=Certificate(ExtraMaterails(dl))
arya=LifetimeAccess(ExtraMaterails(Mentorship(Certificate(ds))))

print(f"{'-'*7} Online Learining Course System {'-'*7}")


print("Student: Jon Snow")
print(jon.description())
print('-'*30)
print(f"Total cost: {jon.cost()}$")

print('*'*40)
print("Student: Rob Stark")
print(rob.description())
print('-'*30)
print(f"Total cost: {rob.cost()}$")

print('*'*40)
print("Student: Arya Stark")
print(arya.description())
print('-'*30)
print(f"Total cost: {arya.cost()}$")

