import sys

sys.setrecursionlimit(1500)

a, b, c, d = map(int, input().split())
values = {}


def getParent(children):
    if children == []:
        return 0
    negatives = [child for child in children if child <= 0]
    if negatives != []:  # At least 1 negative (or == 0) child
        return max(negatives) * -1 + 1
    else:  # No negative child
        return (max(children) + 1) * -1


def getMirrorRotation(wIn, hIn, xIn, yIn):
    if wIn < hIn:
        w = hIn
        h = wIn
        x = yIn
        y = wIn - xIn - 1
    else:
        w = wIn
        h = hIn
        x = xIn
        y = yIn
    if x > w // 2:
        x = w - x - 1
    if y > h // 2:
        y = h - y - 1
    return [w, h, x, y]


def getVal(w, h, x, y):
    w, h, x, y = getMirrorRotation(w, h, x, y)
    value = "[" + str(w) + " " + str(h) + " " + str(x) + " " + str(y) + "]"
    assert x < w and y < h
    if value not in values:
        if w == h and w % 2 == 1 and (
                    (x == 0 and y == h // 2) or (y == 0 and x == w // 2) or (x == w // 2 and y == h - 1) or (
                y == h // 2 and x == w - 1)):
            values.update({value: w})
        else:
            children = []
            for i in range(1, w):
                if i <= x:
                    children.append(getVal(w - i, h, x - i, y))
                else:
                    children.append(getVal(i, h, x, y))
            for j in range(1, h):
                if j <= y:
                    children.append(getVal(w, h - j, x, y - j))
                else:
                    children.append(getVal(w, j, x, y))
            values.update({value: getParent(children)})
    return values[value]


print(getVal(a, b, c, d))
'''
n = 11
for i in range(n):
    for j in range(n):
        values = {}
        val = getVal(n, n, i, j)
        if val == n:
            print(n, n, i, j, val)


10 7 7 3 = 11
3 2 2 0 = 3
100 100 50 50 = -198
100 100 48 52 = 191

Q6.

'''
