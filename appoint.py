from time import time

startTime = time()
# nbScenarios = int(input())
# scenarios = []
# for _ in range(nbScenarios):
#    price = int(input())
#    nbCoins = int(input())
#    coins = []
#    for _ in range(nbCoins):
#       coins.append(int(input())) #Sort?
#    scenarios.append([price, nbCoins, coins])

nbScenarios = 1
scenarios = [[1400, 3, [500, 1000, 2000]]]

for scenario in scenarios:
    payed = 0
    coinsUsed = 0
    price, nbCoins, coins = scenario
    for i in range(nbCoins - 1, -1, -1):
        if coins[i] == price:
            print(str(price) + " 1")
        elif coins[i] < price:
            a=1
            # I have to go recursive for this one, or dynamic

    print(" ".join(map(str, [payed, coinsUsed])))

endTime = time()

print(endTime - startTime)
# 0.02
