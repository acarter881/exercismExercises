# Globals for the directions
EAST = 'EAST'
NORTH = 'NORTH'
WEST = 'WEST'
SOUTH = 'SOUTH'

"""
The robots have three possible movements:
    turn right -> "R"
    turn left  -> "L"
    advance    -> "A"
"""

class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self.direction = direction
        self.x = x
        self.y = y
        self.coordinates = (x,y)

    def move(self, letters):
        for letter in letters:
            if self.direction == NORTH and letter == 'R':
                self.direction = EAST
            elif self.direction == NORTH and letter == 'L':
                self.direction = WEST
            elif self.direction == NORTH and letter == 'A':    # We'll remain facing NORTH
                self.y += 1 
                self.coordinates = (self.x, self.y)
            elif self.direction == EAST and letter == 'R':
                self.direction = SOUTH
            elif self.direction == EAST and letter == 'L':
                self.direction = NORTH
            elif self.direction == EAST and letter == 'A':     # We'll remain facing EAST
                self.x += 1
                self.coordinates = (self.x, self.y) 
            elif self.direction == SOUTH and letter == 'R':
                self.direction = WEST
            elif self.direction == SOUTH and letter == 'L':
                self.direction = EAST
            elif self.direction == SOUTH and letter == 'A':   # We'll remain facing SOUTH
                self.y -= 1
                self.coordinates = (self.x, self.y) 
            elif self.direction == WEST and letter == 'R':
                self.direction = NORTH
            elif self.direction == WEST and letter == 'L':
                self.direction = SOUTH
            elif self.direction == WEST and letter == 'A':    # We'll remain facing WEST
                self.x -= 1
                self.coordinates = (self.x, self.y) 