# Mini Operating System Simulator

This project is a terminal-based educational operating system simulator.
It demonstrates the main operating system concepts covered during the course by using simple Python simulations.

The simulator includes process management, CPU scheduling, memory management, concurrency, disk scheduling, RAID, file system operations, crash consistency, and SSD vs HDD analysis.

## Project Purpose

The purpose of this project is to show how core operating system concepts work through small and understandable simulations.
Each module focuses on a different topic and prints the simulation steps and results to the terminal.

## Implemented Modules

### Module 1 — Process Management

* Process creation
* Process states
* Process termination
* Process Control Block simulation

### Module 2 — CPU Scheduling

* First Come First Served
* Round Robin
* Multi-Level Feedback Queue
* Gantt chart generation
* Waiting time calculation
* Turnaround time calculation
* Algorithm comparison

### Module 3 — Address Translation

* Virtual address simulation
* Physical address calculation
* Base and limit register checking

### Module 4 — Segmentation

* Segment table
* Logical-to-physical address translation
* Segment limit checking

### Module 5 — Paging

* Page table
* Page number and offset calculation
* Page lookup
* Page fault demonstration

### Module 6 — TLB

* TLB hit
* TLB miss
* TLB update
* Hit ratio calculation

### Module 7 — Page Replacement

* FIFO page replacement
* LRU page replacement
* Page fault rate comparison

### Module 8 — Concurrency

* Multithreaded simulation
* Race condition demonstration
* Correct synchronization demonstration

### Module 9 — Locks

* Mutex lock implementation
* Shared resource protection

### Module 10 — Semaphores and Condition Variables

* Producer-consumer problem
* Semaphore-based synchronization
* Bounded buffer simulation

### Module 11 — Concurrent Data Structures

* Thread-safe queue
* Producer and consumer threads
* Condition variable usage

### Module 12 — Disk Scheduling

* FCFS disk scheduling
* SSTF disk scheduling
* Total head movement calculation

### Module 13 — RAID

* RAID 0 simulation
* RAID 1 simulation
* Storage usage comparison
* Fault tolerance demonstration

### Module 14 — File System

* Directory creation
* File creation
* File deletion
* File lookup
* File system tree display

### Module 15 — Crash Consistency

* Simple journaling mechanism
* Simulated crash
* Recovery after crash

### Module 16 — SSD vs HDD Analysis

* Performance comparison
* Access time estimation
* Discussion from operating system perspective

## Technologies Used

* Python 3
* Threading module
* Collections module
* Terminal-based user interface

## Project Structure

```text
mini_os_simulator/
│
├── main.py
├── README.md
│
└── modules/
    ├── process_management.py
    ├── cpu_scheduling.py
    ├── address_translation.py
    ├── segmentation.py
    ├── paging.py
    ├── tlb.py
    ├── page_replacement.py
    ├── concurrency.py
    ├── locks.py
    ├── semaphores.py
    ├── thread_safe_queue.py
    ├── disk_scheduling.py
    ├── raid.py
    ├── file_system.py
    ├── crash_consistency.py
    └── ssd_hdd_analysis.py
```

## How to Run

First, open the project folder in the terminal.

```bash
cd mini_os_simulator
```

Then run:

```bash
python main.py
```

After running the program, a menu will be displayed.
The user can select any module by entering its number.

Example:

```text
===== MINI OPERATING SYSTEM SIMULATOR =====
1. Process Management
2. CPU Scheduling
3. Address Translation
...
16. SSD vs HDD Analysis
0. Exit
```

## Example Usage

To run the CPU Scheduling module:

```text
Select a module: 2
```

The simulator will display:

* Process list
* FCFS result
* Round Robin result
* MLFQ result
* Gantt charts
* Waiting and turnaround times
* Algorithm comparison

## Notes

This project is designed for educational purposes.
The simulations are simplified versions of real operating system mechanisms.
The goal is to demonstrate the logic behind each concept rather than implementing a complete real operating system.

## Author

Mini Operating System Simulator
Operating Systems Course Project
