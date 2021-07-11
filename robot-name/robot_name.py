import random
from string import ascii_uppercase

class Robot:
    def __init__(self):
        self.name = self.generate_name()

    def reset(self):
        self.name = self.generate_name()
        
    def generate_name(self):
        random.seed()
        return ''.join(random.choices(population=ascii_uppercase, k=2)) + ''.join([str(random.randrange(10)) for i in range(3)])