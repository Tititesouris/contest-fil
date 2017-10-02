# n = int(input())
# bottles = [int(x) for x in input()]

bottles = [10, 5, 1, 1, 8, 2]
n = len(bottles)

outcomes = [
    #[[2, 3, 5, 1], [3, 5, 1, 4]],
    #[[2, 3, 5], [3, 5, 1], [3, 5, 1], [5, 1, 4]]
]
line = []
for i in range(n):
    newbottles = bottles
    line.append([newbottles.pop(i) * n, newbottles])
outcomes.append(line)

bob = max(line[i], line[i+1]) + year *

for year in range(n - 1, 0, -1):
    line = []
    for i in range(year):
        newbottles = outcomes[0][i][1]
        line.append([outcomes[0][i][0] + newbottles.pop(i), newbottles])


print(outcomes)
