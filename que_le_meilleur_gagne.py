# n = int(input())
n = 8
for day in range(1, n):
    teams = [i + day for i in range(n // 2)]
    for team in teams:
        print((team, team + (n // 2)))
