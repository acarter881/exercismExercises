import random

class Character:
    def __init__(self):
        self.strength = self.dexterity = self.constitution = self.intelligence = self.wisdom = self.charisma = sum(sorted([random.randint(1,6) for i in range(4)])[1:])
        self.hitpoints = 10 + modifier(self.constitution)
        
    def ability(self):
        self.ability = random.choices([self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma])[0]
        return self.ability

def modifier(num):
    return (num - 10) // 2
