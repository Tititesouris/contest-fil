m = 3
grid = [
    [1, 2, 0],
    [1, 2, 0],
    [1, 2, 0],
]


def properties():
    for y in range(m):
        color = 0
        count = False
        for x in range(m):
            if grid[y][x] != 0:
                if color != grid[y][x]:
                    return False
                color = grid[y][x]
                count = True
        if not count:
            return False
