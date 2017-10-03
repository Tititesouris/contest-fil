# si sucesseur neg, parent = max des neg *-1 + 1, sinon max * -1 + 1

values = {}
def getVal(w, h, x, y):
    value = "[" + str(w) + " " + str(h) + " " + str(x) + " " + str(y) + "]"
    if value not in values:
        values.update({value: getCurrentVal()})
        for i in range(1, w):
            if x - i >= 0:
                getVal(w - i, h, x - i, y)
            else:
                getVal(w - i, h, x, y)
        for j in range(1, h):
            if y - j >= 0:
                getVal(w, h - j, x, y - j)
            else:
                getVal(w, h - j, x, y)



print(getVal(3, 2, 2, 0))
