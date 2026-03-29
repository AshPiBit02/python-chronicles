# Base Component
class Course:
    def __init__(self,title,base_price):
        self.title=title
        self.base_price=base_price

    def cost(self):
        return self.base_price
    def description(self):
        return self.title
    
# Abstract Decorator
class CourseDecorator(Course):
    def __init__(self,course):
        self.course=course
    def cost(self):
        return self.course.cost()
    def description(self):
        return self.course.description()

# Concrete Decorator(Add-Ons)
class Certificate(CourseDecorator):
    def cost(self):
        return super().cost() + 500
    def description(self):
        return super().description() + "\n Including Certificate(+500$)"
    
class ExtraMaterails(CourseDecorator):
    def cost(self):
        return super().cost() + 300
    def description(self):
        return super().description() + "\nIncluding Notes and Pre-recorded videos(+300$)"
    
class Mentorship(CourseDecorator):
    def cost(self):
        return super().cost() + 1000
    def description(self):
        return super().description() + "\nIncluding Mentorship(+1000$)"

class LifetimeAccess(CourseDecorator):
    def cost(self):
        return super().cost() + 700
    def description(self):
        return super().description() + "Including Limetime Access(+700$)"
    
    