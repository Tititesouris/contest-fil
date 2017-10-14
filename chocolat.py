import sys

sys.setrecursionlimit(1500)

print("Board size: ")
a, b, c, d = map(int, input().split())
values = {}


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
        '''
        This bit of code optimises for Q5, however it makes it impossible to know the moves to get the score
        if w == h and w % 2 == 1 and (
                            (x == 0 and y == h // 2) or (y == 0 and x == w // 2) or (x == w // 2 and y == h - 1) or (
                                y == h // 2 and x == w - 1)):
            values.update({value: {"value": w, "move": []}})
        else:
        '''
        maxPos = 0
        maxNeg = -999999999
        hasNeg = False
        move = []
        result = []
        for i in range(1, w):
            if i <= x:
                val = getVal(w - i, h, x - i, y)
                tempResult = [w - i, h, x - i, y]
            else:
                val = getVal(i, h, x, y)
                tempResult = [i, h, x, y]
            if maxNeg < val <= 0:
                maxNeg = val
                hasNeg = True
                move = [i, 0]
                result = tempResult
            elif 0 <= maxPos < val:
                maxPos = val
                move = [i, 0]
                result = tempResult
        for j in range(1, h):
            if j <= y:
                val = getVal(w, h - j, x, y - j)
                tempResult = [w, h - j, x, y - j]
            else:
                val = getVal(w, j, x, y)
                tempResult = [w, j, x, y]
            if maxNeg < val <= 0:
                maxNeg = val
                hasNeg = True
                move = [0, j]
                result = tempResult
            elif 0 < maxPos < val:
                maxPos = val
                move = [0, j]
                result = tempResult
        if move != []:
            if hasNeg:
                val = maxNeg * -1 + 1
            else:
                val = (maxPos + 1) * -1
        else:
            val = 1
        values.update({value: {"value": val, "move": move, "result": result}})
        return val
    return values[value]["value"]


print("Calculating best moves...")
getVal(a, b, c, d)
gameOver = False
while not gameOver:
    w, h, x, y = getMirrorRotation(a, b, c, d)
    value = "[" + str(w) + " " + str(h) + " " + str(x) + " " + str(y) + "]"
    print("Board:", value)
    print("It's my turn... :thinking:")
    val = values[value]
    v = val["value"]
    turnWin = abs(v) // 2 - 1
    move = val["move"]
    moveMax = max(move)
    result = val["result"]
    print("Splitting " + ("horizontally" if move[0] == 0 else "vertically") + " on the " + str(moveMax) + (
        "st" if moveMax == 1 else "nd" if moveMax == 2 else "rd" if moveMax == 3 else "th") + " crease")
    print("Looks like " + ("I" if v > 0 else "you") + ((" can win in " + str(turnWin) + " more turn" + ("s" if turnWin > 1 else "")) if turnWin > 0 else "'ve won!"))
    print(v)
    print(result)
    break
    gameOver = v == 0

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
