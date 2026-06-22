import random
from collections import deque


def create_sample_processes():
    return [
        {"pid": "P1", "arrival": 0, "burst": 8},
        {"pid": "P2", "arrival": 1, "burst": 4},
        {"pid": "P3", "arrival": 2, "burst": 9},
        {"pid": "P4", "arrival": 3, "burst": 5},
    ]

def create_random_processes():
    process_count = random.randint(4,6)
    processes = []
    for i in range(1, process_count + 1):
        process = {
            "pid": f"P{i}",
            "arrival": random.randint(0, 5),
            "burst": random.randint(2, 10),
        }
        processes.append(process)
 
    return processes

def create_custom_processes():
    processes = []
    process_count = int(input("Enter the number of processes: "))

    for i in range(1, process_count + 1):
        pid = f"P{i}"
        arrival = int(input(f"Enter arrival time for {pid}: "))
        burst = int(input(f"Enter burst time for {pid}: "))
        processes.append({"pid": pid, "arrival": arrival, "burst": burst})

    return processes

def print_processes(processes):
    print("\nProcesses")
    print("---------")
    print("PID\tArrival\tBurst")

    for process in processes:
        print(f"{process['pid']}\t{process['arrival']}\t{process['burst']}")


def print_gantt_chart(gantt_chart):
    print("\nGantt Chart")
    print("-----------")

    chart = ""
    times = ""

    for item in gantt_chart:
        pid, start, end = item
        chart += f"| {pid} "
        times += f"{start:<5}"

    chart += "|"
    times += f"{gantt_chart[-1][2]}"

    print(chart)
    print(times)


def print_result(algorithm_name, processes, gantt_chart, metrics):
    print(f"\n===== {algorithm_name} Result =====")

    print_gantt_chart(gantt_chart)

    print("\nPID\tCompletion\tWaiting\tTurnaround")

    total_waiting = 0
    total_turnaround = 0

    for process in processes:
        pid = process["pid"]
        completion = metrics[pid]["completion"]
        waiting = metrics[pid]["waiting"]
        turnaround = metrics[pid]["turnaround"]

        total_waiting += waiting
        total_turnaround += turnaround

        print(f"{pid}\t{completion}\t\t{waiting}\t{turnaround}")

    average_waiting = total_waiting / len(processes)
    average_turnaround = total_turnaround / len(processes)

    print(f"\nAverage Waiting Time: {average_waiting:.2f}")
    print(f"Average Turnaround Time: {average_turnaround:.2f}")

    return average_waiting, average_turnaround


def fcfs(processes):
    sorted_processes = sorted(processes, key=lambda p: p["arrival"])

    current_time = 0
    gantt_chart = []
    metrics = {}

    for process in sorted_processes:
        pid = process["pid"]
        arrival = process["arrival"]
        burst = process["burst"]

        if current_time < arrival:
            current_time = arrival

        start_time = current_time
        completion_time = current_time + burst
        current_time = completion_time

        turnaround_time = completion_time - arrival
        waiting_time = turnaround_time - burst

        gantt_chart.append((pid, start_time, completion_time))

        metrics[pid] = {
            "completion": completion_time,
            "waiting": waiting_time,
            "turnaround": turnaround_time,
        }

    return gantt_chart, metrics


def round_robin(processes, quantum):
    sorted_processes = sorted(processes, key=lambda p: p["arrival"])    

    ready_queue = deque()   
    remaining_time = {}
    completion_time = {}
    gantt_chart = []

    for process in sorted_processes:
        remaining_time[process["pid"]] = process["burst"]

    current_time = 0
    index = 0
    completed = 0

    while completed < len(sorted_processes):
        while index < len(sorted_processes) and sorted_processes[index]["arrival"] <= current_time:
            ready_queue.append(sorted_processes[index])
            index += 1

        if not ready_queue:
            current_time = sorted_processes[index]["arrival"]
            continue

        process = ready_queue.popleft()
        pid = process["pid"]

        start_time = current_time
        execution_time = min(quantum, remaining_time[pid])
        current_time += execution_time
        remaining_time[pid] -= execution_time

        gantt_chart.append((pid, start_time, current_time))

        while index < len(sorted_processes) and sorted_processes[index]["arrival"] <= current_time:
            ready_queue.append(sorted_processes[index])
            index += 1

        if remaining_time[pid] > 0:
            ready_queue.append(process)
        else:
            completion_time[pid] = current_time
            completed += 1

    metrics = {}

    for process in sorted_processes:
        pid = process["pid"]
        turnaround_time = completion_time[pid] - process["arrival"]
        waiting_time = turnaround_time - process["burst"]

        metrics[pid] = {
            "completion": completion_time[pid],
            "waiting": waiting_time,
            "turnaround": turnaround_time,
        }

    return gantt_chart, metrics 


def mlfq(processes):
    sorted_processes = sorted(processes, key=lambda p: p["arrival"])

    q1 = deque()
    q2 = deque()
    q3 = deque()

    remaining_time = {}
    completion_time = {}
    gantt_chart = []

    for process in sorted_processes:
        remaining_time[process["pid"]] = process["burst"]

    current_time = 0
    index = 0
    completed = 0

    while completed < len(sorted_processes):
        while index < len(sorted_processes) and sorted_processes[index]["arrival"] <= current_time:
            q1.append(sorted_processes[index])
            index += 1

        if not q1 and not q2 and not q3:
            current_time = sorted_processes[index]["arrival"]
            continue

        if q1:
            process = q1.popleft()
            quantum = 2
            level = 1
        elif q2:
            process = q2.popleft()
            quantum = 4
            level = 2
        else:
            process = q3.popleft()
            quantum = remaining_time[process["pid"]]
            level = 3

        pid = process["pid"]
        start_time = current_time
        execution_time = min(quantum, remaining_time[pid])

        current_time += execution_time
        remaining_time[pid] -= execution_time

        gantt_chart.append((pid, start_time, current_time))

        while index < len(sorted_processes) and sorted_processes[index]["arrival"] <= current_time:
            q1.append(sorted_processes[index])
            index += 1

        if remaining_time[pid] == 0:
            completion_time[pid] = current_time
            completed += 1
        else:
            if level == 1:
                q2.append(process)
            elif level == 2:
                q3.append(process)
            else:
                q3.append(process)

    metrics = {}

    for process in sorted_processes:
        pid = process["pid"]
        turnaround_time = completion_time[pid] - process["arrival"]
        waiting_time = turnaround_time - process["burst"]

        metrics[pid] = {
            "completion": completion_time[pid],
            "waiting": waiting_time,
            "turnaround": turnaround_time,
        }

    return gantt_chart, metrics


def compare_algorithms(results):
    print("\n===== Algorithm Comparison =====")
    print(f"{'Algorithm':<15}{'Average Waiting':<20}{'Average Turnaround':<20}")
    print("-" * 55)

    best_algorithm = None
    best_waiting_time = None

    for algorithm_name, result in results.items():
        average_waiting, average_turnaround = result

        print(f"{algorithm_name:<15}{average_waiting:<20.2f}{average_turnaround:<20.2f}")

        if best_waiting_time is None or average_waiting < best_waiting_time:
            best_waiting_time = average_waiting
            best_algorithm = algorithm_name

    print(f"\nBest algorithm based on average waiting time: {best_algorithm}")


def run_cpu_scheduling():
    while True: 
        print("\n--- CPU Scheduling Module ---")
        print("1. Run fixed demo")
        print("2. Run random simulation")
        print("3. Create custom processes")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            processes = create_sample_processes()
        elif choice == "2": 
            processes = create_random_processes()
        elif choice == "3":
            processes = create_custom_processes()
        elif choice == "0":
            break
        else:            
            print("Invalid option.")
            continue

        print_processes(processes)  

        fcfs_gantt, fcfs_metrics = fcfs(processes)
        fcfs_result = print_result("FCFS", processes, fcfs_gantt, fcfs_metrics)

        rr_gantt, rr_metrics = round_robin(processes, quantum=2)
        rr_result = print_result("Round Robin (Quantum=2)", processes, rr_gantt, rr_metrics)

        mlfq_gantt, mlfq_metrics = mlfq(processes)
        mlfq_result = print_result("MLFQ", processes, mlfq_gantt, mlfq_metrics)

        results = {
            "FCFS": fcfs_result,
            "Round Robin": rr_result,
            "MLFQ": mlfq_result,
        }

        compare_algorithms(results)
