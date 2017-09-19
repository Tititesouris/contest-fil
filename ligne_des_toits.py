# n = int(input())
# buildings = []
# for _ in range(n):
#    buildings.append([int(x) for x in input().split()])

n = 6
'''points = [
    [3, 0], [3, 13], [9, 13], [9, 0],
    [1, 0], [1, 11], [5, 11], [5, 0],
    [19, 0], [19, 18], [22, 18], [22, 0],
    [3, 0], [3, 6], [7, 6], [7, 0],
    [16, 0], [16, 3], [25, 3], [25, 0],
    [12, 0], [12, 7], [16, 7], [16, 0]
]'''
'''points = [
    [1, 0], [1, 11], [3, 0], [3, 6], [3, 13], [5, 0], [5, 11], [7, 0], [7, 6], [9, 0], [9, 13], [12, 0],
    [12, 7], [16, 0], [16, 3], [16, 7], [19, 0], [19, 18], [22, 0], [22, 18], [25, 0], [25, 3]
]'''

points = [
    [3, 13, 9],
    [1, 11, 5],
    [19, 18, 22],
    [3, 6, 7],
    [16, 3, 25],
    [12, 7, 16]
]

output = []

'''
def mergeBuildings(a, b):
    rooftop = []
    if b[1] <= a[1]:  # If roof of a is higher than roof of b
        if b[0] < a[0]:  # If left wall of b is not under roof of a
            rooftop.append(b[0])  # Add the left wall of b
            rooftop.append(b[1])  # Add the roof of b until it touches the left wall of a

        rooftop.append(a[0])  # Add the left wall of a
        rooftop.append(a[1])  # Add the roof of a
        rooftop.append(a[2])  # Add the right wall of a

        if a[2] < b[2]:  # If right wall of b is not under roof of a
            rooftop.append(b[1])  # Add the roof of b
            rooftop.append(b[2])  # Add the right wall of b
    return rooftop
'''


# Convert buildings to points
# Remove duplicates
# Sort points in x increasing
# For smallest x, take the point of y 0
# For each x from 1 to n-1, take the point with highest y
# For highest x, take the point of y 0

def getPoint(a, b):
    # Return whoever has smallest x
    if a[0] < b[0]:
        return 0
    if b[0] > a[0]:
        return 1
    # Return whoever has biggest y
    if a[1] > b[1]:
        return 0
    return 1


def mergeBuildings(a, b):
    points = [
        [a[0], 0], [a[0], a[1]], [a[2], a[1]], [a[2], 0],
        [b[0], 0], [b[0], b[1]], [b[2], b[1]], [b[2], 0]
    ]
    point = getPoint(points[0], points[4])
    rooftop = [
        points[point * 4], points[point * 4 + 1]
    ]
    point = getPoint(points[2], points[5])
    if point ==0:
        points.append(points[2])
    if b[1] <= a[1]:  # If roof of a is higher than roof of b
        if b[0] < a[0]:  # If left wall of b is not under roof of a
            rooftop.append(b[0])  # Add the left wall of b
            rooftop.append(b[1])  # Add the roof of b until it touches the left wall of a

        rooftop.append(a[0])  # Add the left wall of a
        rooftop.append(a[1])  # Add the roof of a
        rooftop.append(a[2])  # Add the right wall of a

        if a[2] < b[2]:  # If right wall of b is not under roof of a
            rooftop.append(b[1])  # Add the roof of b
            rooftop.append(b[2])  # Add the right wall of b
    return rooftop


for i in range(len(points)):
    for j in range(len(points)):
        if i != j:
            rooftop = mergeBuildings(points[i], points[j])
            print("Merging " + str(points[i]) + " with " + str(points[j]) + " makes " + str(rooftop))
