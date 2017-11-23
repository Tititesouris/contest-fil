from operator import itemgetter, attrgetter

file = open("test.in", "r")
fileOut = open("test.out", "w")
getInput = file.readline
# getInput = input
m = int(getInput())
n = int(getInput())
jobs = []
for _ in range(n):
    jobs.append(list(map(int, getInput().split())))
output = [0 for _ in range(n)]

# Code starts here
# order [1] from lowest to highest
# order [2] from lowest to highest
sortedJobs = []


def addToSort(item):
    i = 0
    while i < len(sortedJobs) and sortedJobs[i][0] < item[0]:
        i += 1
    sortedJobs.insert(i, item)


i = 0
for job in jobs:
    ratio = job[2] / job[1]
    addToSort([ratio, i])
    i += 1

# SOLUTION \/\/\/\/
# au fur et a mesure du temps, ajouter les job qui sont arrivés a priorityqueue. Trier priorityqueue en permanence selon une heuristique. puis quand il y a suffisemment de serveurs libres pour executer le premier job dans priorityqueue, alors le retirer et l'executer.


t = 0
for sortedJob in sortedJobs:
    t += jobs[sortedJob[1]][2]
    output[sortedJob[1]] = t

# Code ends here

for i in range(n):
    fileOut.write(str(output[i]) + "\n")
