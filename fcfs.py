from process import Process

def simulateFcfs(fileName):
    processes = []
    with open(fileName, "r") as f:
        next(f)  # Skip the header line
        for line in f:
            pid, arrivalTime, burstTime = map(int, line.strip().split(", "))
            processes.append(Process(pid, arrivalTime, burstTime))

    processes.sort(key=lambda p: p.arrivalTime)

    currentTime = 0
    waitingTime = 0
    turnaroundTime = 0
    cpuUsage = 0
    output = []

    for process in processes:
        if process.arrivalTime > currentTime:
            idleTime = process.arrivalTime - currentTime
            output.extend(['idle'] * idleTime)
            currentTime = process.arrivalTime

        output.append(process.pid)
        waitingTime += currentTime - process.arrivalTime
        turnaroundTime += currentTime - process.arrivalTime + process.burstTime
        cpuUsage += process.burstTime
        currentTime += process.burstTime

    avgWaitingTime = waitingTime / len(processes)
    avgTurnaroundTime = turnaroundTime / len(processes)
    cpuUsagePercentage = (cpuUsage / currentTime) * 100

    return output, avgWaitingTime, avgTurnaroundTime, cpuUsagePercentage
