n = int(input())
list = [int(x) for x in input().split()]

max = 0
maxes = {0: -1}
balance = 0
for i in range(n):
    if list[i] == 0:
        balance -= 1
    else:
        balance += 1
    if balance in maxes:
        if i - maxes[balance] > max:
            max = i - maxes[balance]
    else:
        maxes[balance] = i
print(max)