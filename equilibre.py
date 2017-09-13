import timeit
start_time = timeit.default_timer()

def count_zone(a, b):
    c = [0, 0]
    for x in range(a, b):
        c[list[x]] += 1
    return c


n = 9
# n = int(input())
# list = [int(x) for x in input().split()]
list = [0, 1, 0, 0, 0, 1, 1, 1, 0]

max = 0
for start in range(n):
    for stop in range(n, -1, -1):
        count = count_zone(start, stop)
        if abs(count[0] - count[1]) == 0:
            if count[0] + count[1] > max:
                max = count[0] + count[1]

print(max)

elapsed = timeit.default_timer() - start_time
print(elapsed)