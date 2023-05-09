from process import Process

def simulateRr(fileName, timeQuantum):
    processes = []
    with open(fileName, "r") as f:
        next(f)  # Skip the header line
        for line in f:
            pid, arrivalTime, burstTime = map(int, line.strip().split(", "))
            processes.append(Process(pid, arrivalTime, burstTime))

    currentTime = 0
    waitingTime = 0
    turnaroundTime = 0
    cpuUsage = 0
    output = []
    completedProcesses = []

    # Execute processes in a cyclic manner
    while processes:
        process = processes.pop(0)

        if process.arrivalTime > currentTime:
            # Only add idle time if there are no more processes in the queue or if the next process has an arrival time that is later than the current time
            if not processes or processes[0].arrivalTime > currentTime:
                idleTime = process.arrivalTime - currentTime
                output.extend(['idle'] * idleTime)
                currentTime = process.arrivalTime

        # Execute the process for the specified time quantum
        if process.remainingTime <= timeQuantum:
            output.extend([process.pid] * process.remainingTime)
            waitingTime += currentTime - process.arrivalTime
            turnaroundTime += currentTime - process.arrivalTime + process.remainingTime
            cpuUsage += process.remainingTime
            currentTime += process.remainingTime
            process.remainingTime = 0
            completedProcesses.append(process)
        else:
            output.extend([process.pid] * timeQuantum)
            process.remainingTime -= timeQuantum
            cpuUsage += timeQuantum
            currentTime += timeQuantum
            processes.append(process)

    # Calculate performance metrics
    avgWaitingTime = waitingTime / len(completedProcesses)
    avgTurnaroundTime = turnaroundTime / len(completedProcesses)
    cpuUsagePercentage = (cpuUsage / currentTime) * 100

    return output, avgWaitingTime, avgTurnaroundTime, cpuUsagePercentage
