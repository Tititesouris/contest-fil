def ezRemove(list, value):
    try:
        list.remove(value)
    except ValueError:
        pass


k = 2
grid = [
    [1, 2, 3, 4],
    [3, 0, 1, 2],
    [0, 0, 4, 3],
    [4, 3, 2, 0]
]

resultGrid = [[0 for _ in range(k * k)] for _ in range(k * k)]

lines = [list(range(1, k * k + 1)) for _ in range(k * k)]
columns = [list(range(1, k * k + 1)) for _ in range(k * k)]
squares = [list(range(1, k * k + 1)) for _ in range(k * k)]

for y in range(k * k):
    for x in range(k * k):
        if grid[y][x] != 0:
            ezRemove(lines[y], grid[y][x])
            ezRemove(columns[x], grid[y][x])
            ezRemove(squares[(x // k) + (y // k) * k], grid[y][x])


def verify(_grid, _lines, _columns, _squares):
    noZeros = True
    for y in range(k * k):
        for x in range(k * k):
            if _grid[y][x] == 0:
                noZeros = False
                possibleValues = list(
                    set.intersection(set(_lines[y]), set(_columns[x]), set(_squares[(x // k) + (y // k) * k]))
                )
                success = False
                for v in possibleValues:
                    ngrid = _grid
                    ngrid[y][x] = v
                    nlines = _lines
                    ncolumns = _columns
                    nsquares = _squares
                    ezRemove(nlines, v)
                    ezRemove(ncolumns, v)
                    ezRemove(nsquares, v)
                    if verify(ngrid, nlines, ncolumns, nsquares):
                        success = True
                        _grid = ngrid
                        _lines = nlines
                        _columns = ncolumns
                        _squares = nsquares
                        break
                if not success:
                    return False

    if noZeros:
        return True


print(verify(grid, lines, columns, squares))
