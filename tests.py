'''
k = 2
n = 2
houses = [0, 4]


def f(houses, k):
    a = 0
    b = 0
    r = int(n > 0)
    for i in range(n):
        if houses[b] - houses[a] <= 2 * k:
            b += 1
        else:
            r += 1
            a = b + 1
            b = a
    return r


print(houses)
print(f(houses, k))
'''

n = 3
records = [12, 26, 19]
print(sorted(records))
