from app import Shield,DoubleDamage,SpeedBoost,CharacterDecorator,BaseCharacter

if __name__=="__main__":
    ch1=BaseCharacter("Knight",health=100,attack=30,speed=10)

    buffed_ch1=DoubleDamage(SpeedBoost(Shield(ch1)))
    
    print("Final Buffed stats: ")
    for k,v in buffed_ch1.stats().items():
        print(f"{k}: {v}")