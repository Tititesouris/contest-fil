n = int(input())
bottles = [int(x) for x in input().split()]

outcomes = [[[bottles[i] * n, [i]] for i in range(n)]]

for year in range(n - 1, 0, -1):
    line = []
    for i in range(year):
        outcomeA = outcomes[0][i]
        outcomeB = outcomes[0][i + 1]
        toAddA = list(set(outcomeB[1]) - set(outcomeA[1]))[0]
        toAddB = list(set(outcomeA[1]) - set(outcomeB[1]))[0]
        a = outcomeA[0] + year * bottles[toAddA]
        b = outcomeB[0] + year * bottles[toAddB]
        if a >= b:
            line.append([a, [toAddA] + outcomeA[1]])
        else:
            line.append([b, [toAddB] + outcomeB[1]])
    outcomes.insert(0, line)

print(outcomes[0][0][0])
# outcomes[0][0][1] is traceback