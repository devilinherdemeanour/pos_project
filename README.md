# Principle of Operating Systems Project - CPU scheduling algorithms simulator

This project is partial fulfillment of the requirements of the CSCI 3510: Principles of Operating Systems course

Scheduling in Operating System (OS) refers to the process of deciding which tasks (such as processes or threads) should run at what time on a CPU (Central Processing Unit). The purpose of scheduling is to allocate system resources efficiently and effectively to achieve the best possible performance and utilization of the system.

In our project, we simulate 3 different scheduling policies - First-Come-First-Served, Shortest Remaining Time First and Round Robin.

To run the simulator:
1. Clone this repository to your preferred directory using terminal or other tools: `git clone "REPO_LINK"`
2. Create txt file with processes in this structure in the **same directory with the main.py file** and name it `processes.txt`:
    `process_id, arrival_time, running_time
    1, 0, 2
    2, 1, 1`
   P.S - If the name of the file differs, you can change the `fileName` variable inside of the `main.py` file to your file name.
3. Simply run `main.py`. It will generate 3 txt files in the same directory as the project with the results

There are 6 Python files. `fcfs.py`, `rr.py` and `srtf.py` refer to algorithm structures, `process.py` is a class 
that shows the structure of each process and `file.py` creates "txt" files that shows the outputs of each algorithm.

All of the logic is executed in `main.py`.
