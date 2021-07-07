SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        if ','.join(map(str, list_two)) == ','.join(map(str, list_one)):
            return EQUAL
        return UNEQUAL
    
    if len(list_one) > len(list_two):
        if ','.join(map(str, list_two)) in ','.join(map(str, list_one)):
            return SUPERLIST
        return UNEQUAL

    if len(list_one) < len(list_two):
        if ','.join(map(str, list_one)) in ','.join(map(str, list_two)):
            return SUBLIST
        return UNEQUAL