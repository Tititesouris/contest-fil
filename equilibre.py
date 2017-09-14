import timeit

start_time = timeit.default_timer()

c = 0
n = 14
# n = int(input())
# list = [int(x) for x in input().split()]
list = [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
# 1.5
'''
list = [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1,
        0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0,
        0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
        
def balance(number):
    if number == 0:
        return -1
    else:
        return 1


def count_zone(a, b):
    total = 0
    for x in range(a, b):
        total += balance(list[x])
    return total


max = 0
start = -1
end = -1

balanceLeft = [balance(list[0])]
balanceRight = [balance(list[n - 1])]
test = ["#"]
test2 = []
for i in range(1, n):
    balanceLeft.append(balanceLeft[i - 1] + balance(list[i]))
    balanceRight.insert(0, balanceRight[0] + balance(list[n - i - 1]))
    test.append(balanceLeft[i] - balanceLeft[abs(balanceLeft[i]) - 1])
    test2.append(balanceLeft[i] + balanceRight[i])

print(balanceLeft)
print(balanceRight)
print(test)
print(test2)
print(max)
# First pass where every block of 0 and every block of 1 is marked
# 0, 1, 1, 0 becomes

clusters = [[list[0], 1]]
cluster = 0
for i in range(1, n):
    if list[i] == clusters[cluster][0]:
        clusters[cluster][1] += 1
    else:
        clusters.append([list[i], 1])
        cluster += 1

change = True
while change:
    print(clusters)
    newClusters = []
    for i in range(1, len(clusters)):
        cluster = clusters[i]
        if cluster[1] == clusters[i - 1][1]:
            newClusters.append([cluster[0], cluster[1] + clusters[i - 1][1]])
def getMax():
    max = 0
    for start in range(nbClusters):
        for stop in range(nbClusters, -1, -1):
            balance = getBalance(start, stop)
            if balance == 0:
                if stop - start > max:
                    max = stop - start
                    break
        if max >= n - start:
            return max
    return max


def getBalance(start, stop):
    balance = 0
    for i in range(start, stop):
        if list[i] == 0:
            balance -= 1
        else:
            balance += 1
    return balance


def getMax():
    max = 0
    for start in range(n):
        for stop in range(n, -1, -1):
            balance = getBalance(start, stop)
            if balance == 0:
                if stop - start > max:
                    max = stop - start
                    break
        if max >= n - start:
            return max
    return max

'''


def getBalance(position):
    if list[position] == 0:
        return -1
    return 1


max = 0
start = -1
end = -1

balanceLeft = [getBalance(0)]
for i in range(1, n):
    balanceLeft.append(balanceLeft[i - 1] + getBalance(i))
    if abs(balanceLeft[i] - i) > 1:
        if i - start + 1 > max:
            max = i - start + 1
            print(abs(balanceLeft[i] - i))
        start = i

print(balanceLeft)
print(max)

elapsed = timeit.default_timer() - start_time
print(elapsed)
print(elapsed < 0.003)
