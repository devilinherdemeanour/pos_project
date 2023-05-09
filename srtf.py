from process import Process

def simulateSrtf(fileName):
    processes = []
    with open(fileName, "r") as f:
        next(f)  # Skip the header line
        for line in f:
            pid, arrivalTime, burstTime = map(int, line.strip().split(", "))
            processes.append(Process(pid, arrivalTime, burstTime))

    completedProcesses = []
    currentTime = 0
    waitingTime = 0
    turnaroundTime = 0
    cpuUsage = 0
    output = []

    while processes:
        eligibleProcesses = [p for p in processes if p.arrivalTime <= currentTime and p.remainingTime > 0]

        if not eligibleProcesses:
            output.append('idle')
            currentTime += 1
            continue

        shortestProcess = min(eligibleProcesses, key=lambda p: p.remainingTime)

        output.append(shortestProcess.pid)
        cpuUsage += 1

        shortestProcess.remainingTime -= 1
        currentTime += 1

        if shortestProcess.remainingTime == 0:
            completedProcesses.append(shortestProcess)
            waitingTime += currentTime - shortestProcess.arrivalTime - shortestProcess.burstTime
            turnaroundTime += currentTime - shortestProcess.arrivalTime
            processes.remove(shortestProcess)

    avgWaitingTime = waitingTime / len(completedProcesses)
    avgTurnaroundTime = turnaroundTime / len(completedProcesses)
    cpuUsagePercentage = (cpuUsage / currentTime) * 100

    return output, avgWaitingTime, avgTurnaroundTime, cpuUsagePercentage
