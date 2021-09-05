PAIRS = dict(("{}", "()", "[]"))
OPENERS = PAIRS.keys()
CLOSERS = PAIRS.values()

def is_paired(brackets):
    stack = []

    for char in brackets:
        if char in OPENERS:
            stack.append(char)
        elif char in CLOSERS:
            if not stack or PAIRS[stack.pop()] != char:
                return False

    return not stack