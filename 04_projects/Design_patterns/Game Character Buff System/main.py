from app import Shield,DoubleDamage,SpeedBoost,CharacterDecorator,BaseCharacter,battle

if __name__=="__main__":
    ch1=BaseCharacter("Knight",health=100,attack=30,speed=10)

    buffed_ch1=Shield(DoubleDamage(SpeedBoost(Shield(ch1))))
    
    print("Final Buffed stats: ")
    for k,v in buffed_ch1.stats().items():
        print(f"{k}: {v}")



    Knight1=BaseCharacter("Knight A",health=100,attack=30,speed=10)
    Knight2=BaseCharacter("Knight B",health=120,attack=25,speed=15)

    buffed_knight1=DoubleDamage(SpeedBoost(Shield(Knight1)))
    buffed_knight2=Shield(Knight2)

    battle(buffed_knight1,buffed_knight2)

