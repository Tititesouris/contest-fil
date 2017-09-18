n = int(input())
list = [int(x) for x in input().split()]

max = 0
counter = {}
for i in range(n):
    item = list[i]
    if item in counter:
        counter[item] += 1
        if counter[item] > max:
            max = counter[item]
    else:
        counter[item] = 1

if max > n / 2:
    for item, amount in counter.items():
        if amount == max:
            print(item)
            break
else:
    print(-1)