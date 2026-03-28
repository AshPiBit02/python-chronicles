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
    
    def take_damage(self,amount):
        self.health-=amount
        if self.health < 0:
            self.health =0
    
    def is_alive(self):
        return self.health > 0
    
# Abstract Decorator
class CharacterDecorator(BaseCharacter):
    def __init__(self,character):
        self.character=character
    
    def stats(self):
        return self.character.stats()
    
    def take_damage(self, amount):
        self.character.take_damage(amount)

    def is_alive(self):
        return self.character.is_alive()
    
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

# Battle Simulation
def battle(char1,char2):
    print(f"{'-'*7} Battle Start {'-'*7}")
    print(char1.stats())
    print(char2.stats())
    print('-'*40)

    while char1.is_alive() and char2.is_alive():
        if char1.stats()["Speed"] >= char2.stats()["Speed"]:
            attacker,defender=char1,char2
        else:
            attacker,defender=char2,char1
        
        # Attack
        damage=attacker.stats()["Attack"]
        defender.take_damage(damage)
        print(f"{attacker.stats()["Name"]} attacks {defender.stats()["Name"]} for {damage} damage!")
    
        print(f"{defender.stats()["Name"]} health: {defender.stats()["Health"]}")
        print('-'*35)
        if not defender.is_alive():
            print(f"{defender.stats()["Name"]} has been defeated!")
            break
        
