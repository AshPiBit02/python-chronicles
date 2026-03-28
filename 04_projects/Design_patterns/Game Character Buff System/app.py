# Base Component
class BaseCharacter:
    def __init__(self,name,health,attack,speed):
        self.name=name
        self.health=health
        self.attack=attack
        self.speed=speed
    
    def stats(self):
        return {
            "Name":self.name,
            "Health":self.health,
            "Attack":self.attack,
            "Speed":self.speed
        }
    
# Abstract Decorator
class CharacterDecorator(BaseCharacter):
    def __init__(self,character):
        self.character=character
    
    def stats(self):
        return self.character.stats()
    
# Concrete Decorator
class SpeedBoost(CharacterDecorator):
    def stats(self):
        base_stats=super().stats()
        base_stats["Speed"]+=20
        return base_stats
    
class Shield(CharacterDecorator):
    def stats(self):
        base_stats=super().stats()
        base_stats["Health"]+=50
        return base_stats
    
class DoubleDamage(CharacterDecorator):
    def stats(self):
        base_stats=super().stats()
        base_stats["Attack"] *=2
        return base_stats
