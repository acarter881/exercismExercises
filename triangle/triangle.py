def equilateral(sides):
    return all(x == sides[0] and x != 0 for x in sides)

def isosceles(sides):
    if isValidTriangle(sides):
        a, b, c = sides[0], sides[1], sides[2]
        if a == b or b == c or a == c or a==b==c: return True
        return False
    return False
        
def scalene(sides):
    if isValidTriangle(sides):
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]: return True
        return False
    return False

def isValidTriangle(sides):
    a, b, c = sides[0], sides[1], sides[2]
    if a + b >= c and b + c >= a and a + c >=b: return True