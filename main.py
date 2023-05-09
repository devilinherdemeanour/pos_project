import fcfs
import rr 
import srtf
import file


fileName = "processes.txt"

fcfsOutput, fcfsAvgWaitingTime, fcfsAvgTurnaroundTime, fcfsCpuUsage = fcfs.simulateFcfs(fileName)
srtfOutput, srtfAvgWaitingTime, srtfAvgTurnaroundTime, srtfCpuUsage = srtf.simulateSrtf(fileName)
rrOutput, rrAvgWaitingTime, rrAvgTurnaroundTime, rrCpuUsage = rr.simulateRr(fileName, 3)

file.generateOutputFile("teamoo7_FCFS.txt", fcfsOutput, fcfsAvgWaitingTime, fcfsAvgTurnaroundTime, fcfsCpuUsage)
file.generateOutputFile("teamoo7_SRTF.txt", srtfOutput, srtfAvgWaitingTime, srtfAvgTurnaroundTime, srtfCpuUsage)
file.generateOutputFile("teamoo7_RR.txt", rrOutput, rrAvgWaitingTime, rrAvgTurnaroundTime, rrCpuUsage)
