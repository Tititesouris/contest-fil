# si sucesseur neg, parent = max des neg *-1 + 1, sinon max * -1 + 1

def getVal(w, h, x, y):
    values = {}
    for i in range(1, w):
        if x - i >= 0:
            values.update(getVal(w - i, h, x - i, y))
        else:
            values.update(getVal(w - i, h, x, y))
    for j in range(1, h):
        if y - j >= 0:
            values.update(getVal(w, h - j, x, y - j))
        else:
            values.update(getVal(w, h - j, x, y))
    return {"[" + str(w) + " " + str(h) + " " + str(x) + " " + str(y) + "]": values}


print(getVal(3, 2, 2, 0))
