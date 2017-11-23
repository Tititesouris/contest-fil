import random
file = open("data.in", "r")

nbNodes, nbStreets, totalTimeAvailable, nbCars, startNode = map(int, file.readline().split())

nodes = []
for iNode in range(nbNodes):
    lat, long = map(float, file.readline().split())
    nodes.append({"lat": lat, "long": long})

streets = []
for iStreet in range(nbStreets):
    nodeA, nodeB, direction, time, length = map(int, file.readline().split())
    streets.append({"a": nodeA, "b": nodeB, "bi": direction == 2, "time": time, "length": length})


tree = {}
for street in streets:
    if street["a"] not in tree:
        tree[street["a"]] = []
    if all([node["branch"] != street for node in tree[street["a"]]]):
        tree[street["a"]].append({"branch": street, "leaf": street["b"]})
    if street["bi"]:
        if street["b"] not in tree:
            tree[street["b"]] = []
        if all([node["branch"] != street for node in tree[street["b"]]]):
            tree[street["b"]].append({"branch": street, "leaf": street["a"]})


visitedNodes = []
visitedStreets = []
for iCar in range(nbCars):
    currentNode = startNode
    carVisited = []
    leftoverTime = totalTimeAvailable
    deadEnd = False
    while not deadEnd and leftoverTime > 0:
        deadEnd = True

        toVisit = None
        for node in tree[currentNode]:
            if node["branch"] not in visitedStreets and leftoverTime >= node["branch"]["time"]:
                toVisit = node
                break

        if toVisit == None:
            toVisit = tree[currentNode][random.randint(0, len(tree[currentNode])-1)]
        if leftoverTime >= toVisit["branch"]["time"]:
            carVisited.append(toVisit["leaf"])
            visitedStreets.append(toVisit["branch"])
            currentNode = toVisit["leaf"]
            leftoverTime -= toVisit["branch"]["time"]
            deadEnd = False
            break
    visitedNodes.append(carVisited)


print(tree)

outFile = open("data.out", "w")
nbCarsUsed = len(visitedNodes)
outFile.write(str(nbCarsUsed) + "\n")
for iCarUsed in range(nbCarsUsed):
    nbNodesVisited = len(visitedNodes[iCarUsed]) + 1
    outFile.write(str(nbNodesVisited) + "\n")
    outFile.write(str(startNode) + "\n")
    for iNodeVisited in range(nbNodesVisited - 1):
        outFile.write(str(visitedNodes[iCarUsed][iNodeVisited]) + "\n")
