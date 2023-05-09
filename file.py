def generateOutputFile(fileName, output, avgWaitingTime, avgTurnaroundTime, cpuUsagePercentage):
    with open(fileName, 'w') as f:
        for i, processId in enumerate(output):
            f.write(f"time {i}: running process: {processId}\n")
        f.write(f"Average waiting time: {avgWaitingTime}\n")
        f.write(f"Average turnaround time: {avgTurnaroundTime}\n")
        f.write(f"Average CPU usage: {cpuUsagePercentage:.2f}%\n")