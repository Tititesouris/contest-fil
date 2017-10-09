def getParent(children):
    if children == []:
        return 0
    negatives = [child for child in children if child <= 0]
    if negatives != []:  # At least 1 negative (or == 0) child
        return max(negatives) * -1 + 1
    else:  # No negative child
        return (max(children) + 1) * -1


def getVal(w, h, x, y, values):
    value = "[" + str(w) + " " + str(h) + " " + str(x) + " " + str(y) + "]"
    if value not in values:
        # if w == h
        children = []
        for i in range(1, w):
            if x - i >= 0:
                children.append(getVal(w - i, h, x - i, y, values))
            else:
                children.append(getVal(w - i, h, x, y, values))
        for j in range(1, h):
            if y - j >= 0:
                children.append(getVal(w, h - j, x, y - j, values))
            else:
                children.append(getVal(w, h - j, x, y, values))
        values.update({value: getParent(children)})
    return values[value]


print("test")
n = 7
for i in range(n):
    for j in range(n):
        print(getVal(n, n, i, j, {}))

print(getVal(10, 7, 7, 3, {})) # devrait etre 11