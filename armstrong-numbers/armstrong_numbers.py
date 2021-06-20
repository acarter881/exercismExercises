def is_armstrong_number(number):
    if sum((int(str(number)[i])**len(str(number)) for i in range(len(str(number))))) == number: return True
    return False