import math

# n = int(input())
# buildings = []
# for _ in range(n):
#    buildings.append([int(x) for x in input().split()])

n = 6
points = [
    [3, 13, 9],
    [1, 11, 5],
    [19, 18, 22],
    [3, 6, 7],
    [16, 3, 25],
    [12, 7, 16]
]

'''points = [
    [[3, 0], [3, 13], [9, 13], [9, 0]],
    [[1, 0], [1, 11], [5, 11], [5, 0]],
    [[19, 0], [19, 18], [22, 18], [22, 0]],
    [[3, 0], [3, 6], [7, 6], [7, 0]],
    [[16, 0], [16, 3], [25, 3], [25, 0]],
    [[12, 0], [12, 7], [16, 7], [16, 0]]
]'''

def mergeBuildings(rooftop, building):
    if rooftop == []:
        return [
            [building[0], 0],
            [building[0], building[1]],
            [building[2], building[1]],
            [building[2], 0]
        ]

    if building[0] < rooftop[0][0]:
        rooftop.insert(0, [building[0], 0])
        rooftop.insert(1, [building[0], building[1]])
    elif building[0] == rooftop[0][0] and building[1] > rooftop[1][1]:
        rooftop.insert(1, [building[0], building[1]])
    return rooftop

rooftop = []
for i in range(n):
    rooftop = mergeBuildings(rooftop, points[i])
    print(rooftop)
