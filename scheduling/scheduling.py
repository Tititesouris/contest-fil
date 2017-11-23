m = 0
n = 0
jobs = []  # List of jobs


def getInput():
    global m, n, jobs
    file = open("nancy.in", "r")
    m = int(file.readline())  # Number of machines
    n = int(file.readline())  # Number of jobs
    jobs = []  # List of jobs
    for i in range(n):  # Each job is [arrivalTime, nbCPUNeeded, length, order]
        jobs.append(list(map(int, (file.readline() + " " + str(i)).split())))


getInput()

# Code starts here

output = [0 for _ in range(n)]
waitingJobs = []
runningJobs = []
freeCPUs = m


def compareJobs(jobA, jobB):  # Heuristic
    return (jobB[1] - jobA[1]) + (jobB[2] - jobA[2])


def addWaitingJob(job):
    i = 0
    for waitingJob in waitingJobs:
        if compareJobs(waitingJob, job) >= 0:
            break
        i += 1
    waitingJobs.insert(i, job)


time = 0
while len(jobs) > 0 or len(waitingJobs) > 0 or len(runningJobs) > 0:
    for i in range(len(jobs) - 1, -1, -1):
        job = jobs[i]
        if job[0] == time:  # Job arrived
            addWaitingJob(jobs.pop(i))

    for i in range(len(waitingJobs) - 1, -1, -1):
        waitingJob = waitingJobs[i]
        if freeCPUs >= waitingJob[1]:
            freeCPUs -= waitingJob[1]
            output[waitingJob[3]] = time
            runningJobs.append(waitingJobs.pop(i))

    for i in range(len(runningJobs) - 1, -1, -1):
        runningJob = runningJobs[i]
        runningJob[2] -= 1
        if runningJob[2] <= 0:
            freeCPUs += runningJob[1]
            runningJobs.pop(i)
    time += 1


# Code ends here

def setOutput():
    fileOut = open("nancy.out", "w")
    for i in range(n):
        fileOut.write(str(output[i]) + "\n")


setOutput()
