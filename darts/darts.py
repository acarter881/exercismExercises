def score(x, y):
    myCirclePoint = (x - 0) ** 2 + (y - 0) ** 2

    if myCirclePoint <= 1: return 10
    elif myCirclePoint > 1 and myCirclePoint <= 25: return 5
    elif myCirclePoint > 25 and myCirclePoint <= 100: return 1
    else: return 0