# Base Component
class Course:
    def __init__(self,title,base_price):
        self.title=title
        self.base_price=base_price

    def cost(self):
        return self.base_price
    def description(self):
        return f"Course Title: {self.title}"
    
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
        return super().description() + f"\nIncluding Certificate(+500$)"
    
class ExtraMaterails(CourseDecorator):
    def cost(self):
        return super().cost() + 300
    def description(self):
        return super().description() + f"\nIncluding Notes and Pre-recorded videos(+300$)"
    
class Mentorship(CourseDecorator):
    def cost(self):
        return super().cost() + 1000
    def description(self):
        return super().description() + f"\nIncluding Mentorship(+1000$)"

class LifetimeAccess(CourseDecorator):
    def cost(self):
        return super().cost() + 700
    def description(self):
        return super().description() + f"\nIncluding Limetime Access(+700$)"
    
class Quizes_Assessments(CourseDecorator):
    def cost(self):
        return super().cost() + 200
    def description(self):
        return super().description() + f"\nQuizzes & Assessments(+200$)"
    
class Community_access(CourseDecorator):
    def cost(self):
        return super().cost() + 150
    def description(self):
        return super().description() + f"\nCommunity Access(+150$)"
    
class Downloadable_resources(CourseDecorator):
    def cost(self):
        return super().cost() + 100
    def description(self):
        return super().description() + f"\nIncluding Downloadable Resources(+100$)"
    
class One_on_One_Coaching(CourseDecorator):
    def cost(self):
        return super().cost() + 2000
    def description(self):
        return super().description() + f"\nIncluding One-on-One Coaching(+2000$)"
    
class Job_Assistance(CourseDecorator):
    def cost(self):
        return super().cost() + 12000
    def description(self):
        return super().description() + f"\nIncluding Job Assistance(+1200$)"
    
class Group_Projects(CourseDecorator):
    def cost(self):
        return super().cost() + 800
    def description(self):
        return super().description() + f"\nIncluding Capstone Project(+800$)"
    
class Multi_Language_subtitles(CourseDecorator):
    def cost(self):
        return super().cost() + 20
    def description(self):
        return super().description() + f"\nIncluding Multi-Language Subtitles"
    

    
    