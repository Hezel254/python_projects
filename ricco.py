import random

class Dice:
#defn functions to take place under the class
    def roll():
        
        f_roll= random.randint(1,6)
        l_roll=random.randint(1,6)
        return f_roll,l_roll

dice= Dice
print(dice.roll())







