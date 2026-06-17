import random

def calculate_movement(from_position, to_position):
    return abs(to_position - from_position)


def fcfs_disk_scheduling(requests, initial_head):
    print("\n===== FCFS Disk Scheduling =====")
    print("Requests are served in the order they arrive.")

    current_head = initial_head
    total_head_movement = 0
    sequence = [initial_head]

    for request in requests:
        movement = calculate_movement(current_head, request)
        total_head_movement += movement

        print(f"Move from {current_head} to {request} | Movement: {movement}")

        current_head = request
        sequence.append(request)

    print("\nFCFS Summary")
    print("------------")
    print(f"Service Sequence: {sequence}")
    print(f"Total Head Movement: {total_head_movement}")

    return sequence, total_head_movement


def sstf_disk_scheduling(requests, initial_head):
    print("\n===== SSTF Disk Scheduling =====")
    print("The closest request to the current head position is served first.")

    pending_requests = requests.copy()
    current_head = initial_head
    total_head_movement = 0
    sequence = [initial_head]

    while pending_requests:
        closest_request = min(
            pending_requests,
            key=lambda request: calculate_movement(current_head, request)
        )

        movement = calculate_movement(current_head, closest_request)
        total_head_movement += movement

        print(f"Move from {current_head} to {closest_request} | Movement: {movement}")

        current_head = closest_request
        sequence.append(closest_request)
        pending_requests.remove(closest_request)

    print("\nSSTF Summary")
    print("------------")
    print(f"Service Sequence: {sequence}")
    print(f"Total Head Movement: {total_head_movement}")

    return sequence, total_head_movement


def compare_algorithms(fcfs_result, sstf_result):
    fcfs_sequence, fcfs_movement = fcfs_result
    sstf_sequence, sstf_movement = sstf_result

    print("\n===== Disk Scheduling Comparison =====")
    print("Algorithm\tTotal Head Movement")
    print(f"FCFS\t\t{fcfs_movement}")
    print(f"SSTF\t\t{sstf_movement}")

    if fcfs_movement < sstf_movement:
        print("\nFCFS performed better for this request sequence.")
    elif sstf_movement < fcfs_movement:
        print("\nSSTF performed better because it reduced total head movement.")
    else:
        print("\nBoth algorithms had the same total head movement.")


def run_demo():
    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    initial_head = 53

    print("\n--- Disk Scheduling Demo ---")
    print(f"Initial Head Position: {initial_head}")
    print(f"Disk Requests: {requests}")

    fcfs_result = fcfs_disk_scheduling(requests, initial_head)
    sstf_result = sstf_disk_scheduling(requests, initial_head)

    compare_algorithms(fcfs_result, sstf_result)

def run_random_simulation():
    request_count = random.randint(6, 10)
    max_cylinder = 199

    requests = [
        random.randint(0, max_cylinder)
        for _ in range(request_count)
    ]

    initial_head = random.randint(0, max_cylinder)

    print("\n--- Random Disk Scheduling Simulation ---")
    print(f"Initial Head Position: {initial_head}")
    print(f"Disk Requests: {requests}")

    fcfs_result = fcfs_disk_scheduling(requests, initial_head)
    sstf_result = sstf_disk_scheduling(requests, initial_head)

    compare_algorithms(fcfs_result, sstf_result)


def run_custom_simulation():
    try:
        user_input = input("Enter disk requests separated by spaces: ")
        requests = [int(request) for request in user_input.split()]

        initial_head = int(input("Enter initial head position: "))

        if len(requests) == 0:
            print("Request list cannot be empty.")
            return

        if initial_head < 0:
            print("Initial head position cannot be negative.")
            return

        for request in requests:
            if request < 0:
                print("Disk request values cannot be negative.")
                return

        fcfs_result = fcfs_disk_scheduling(requests, initial_head)
        sstf_result = sstf_disk_scheduling(requests, initial_head)

        compare_algorithms(fcfs_result, sstf_result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_disk_scheduling():
    while True:
        print("\n--- Disk Scheduling Module ---")
        print("1. Run demo")
        print("2. Enter custom disk requests")
        print("3. Run random simulation")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            run_demo()
        elif choice == "2":
            run_custom_simulation()
        elif choice == "3":
            run_random_simulation()
        elif choice == "0":
            break
        else:
            print("Invalid option.")