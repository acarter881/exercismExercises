def latest(scores):
    return scores[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    myL = []
    try:
        m1 = max(scores)
        scores.remove(m1)
        myL.append(m1)
        m2 = max(scores)
        scores.remove(m2)
        myL.append(m2)
        m3 = max(scores)
        scores.remove(m3)
        myL.append(m3)
    except:
        pass
    return myL