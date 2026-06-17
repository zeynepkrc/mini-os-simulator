def print_comparison_table():
    print("\n===== SSD vs HDD Performance Comparison =====")
    print("Feature\t\t\tHDD\t\t\tSSD")
    print("---------------------------------------------------------------")
    print("Technology\t\tMechanical disk\t\tFlash memory")
    print("Moving Parts\t\tYes\t\t\tNo")
    print("Access Time\t\tHigher\t\t\tLower")
    print("Random Read\t\tSlower\t\t\tFaster")
    print("Sequential Read\t\tGood\t\t\tVery good")
    print("Noise\t\t\tCan be noisy\t\tSilent")
    print("Power Usage\t\tHigher\t\t\tLower")
    print("Durability\t\tSensitive to shock\tMore shock resistant")
    print("Cost per GB\t\tLower\t\t\tHigher")
    print("Common Usage\t\tBackups, archives\tOS, applications, fast storage")


def estimate_access_time(storage_type, operation_count):
    if storage_type == "HDD":
        average_access_time_ms = 10
    elif storage_type == "SSD":
        average_access_time_ms = 0.1
    else:
        return None

    total_time_ms = operation_count * average_access_time_ms
    return total_time_ms


def run_performance_estimation():
    operation_count = 1000

    hdd_time = estimate_access_time("HDD", operation_count)
    ssd_time = estimate_access_time("SSD", operation_count)

    print("\n===== Simple Access Time Estimation =====")
    print(f"Number of Random Access Operations: {operation_count}")
    print(f"Estimated HDD Time: {hdd_time:.2f} ms")
    print(f"Estimated SSD Time: {ssd_time:.2f} ms")

    if ssd_time > 0:
        speedup = hdd_time / ssd_time
        print(f"Estimated SSD Speedup: {speedup:.2f}x faster for random access")

    print("\nNote:")
    print("This is a simplified educational estimation.")
    print("Actual performance depends on device model, workload, interface, cache, and system configuration.")


def print_discussion():
    print("\n===== Discussion =====")

    print("\n1. Performance")
    print("SSDs generally provide faster random access because they do not need mechanical head movement.")
    print("HDDs are slower for random access because the disk head must move to the correct location.")

    print("\n2. Reliability and Durability")
    print("HDDs contain moving parts, so they are more sensitive to drops and physical shock.")
    print("SSDs have no moving parts, so they are usually more resistant to physical movement.")

    print("\n3. Storage Capacity and Cost")
    print("HDDs usually provide larger capacity at a lower cost per GB.")
    print("SSDs are more expensive per GB but provide much better responsiveness.")

    print("\n4. Best Use Cases")
    print("HDDs are suitable for backups, archives, and large media storage.")
    print("SSDs are suitable for operating systems, applications, games, and workloads requiring fast access.")

    print("\n5. Operating System Perspective")
    print("An operating system benefits from SSDs because boot time, application loading, paging, and file access can be faster.")
    print("However, HDD scheduling algorithms are still important for understanding mechanical disk performance.")


def run_custom_estimation():
    try:
        operation_count = int(input("Enter number of random access operations: "))

        if operation_count <= 0:
            print("Operation count must be greater than zero.")
            return

        hdd_time = estimate_access_time("HDD", operation_count)
        ssd_time = estimate_access_time("SSD", operation_count)

        print("\n===== Custom Access Time Estimation =====")
        print(f"Number of Random Access Operations: {operation_count}")
        print(f"Estimated HDD Time: {hdd_time:.2f} ms")
        print(f"Estimated SSD Time: {ssd_time:.2f} ms")

        speedup = hdd_time / ssd_time
        print(f"Estimated SSD Speedup: {speedup:.2f}x faster for random access")

    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def run_demo():
    print("\n--- SSD vs HDD Analysis Demo ---")
    print_comparison_table()
    run_performance_estimation()
    print_discussion()


def run_ssd_hdd_analysis():
    while True:
        print("\n--- SSD vs HDD Analysis Module ---")
        print("1. Run full analysis demo")
        print("2. Run custom access time estimation")
        print("3. Show comparison table")
        print("4. Show discussion")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            run_demo()
        elif choice == "2":
            run_custom_estimation()
        elif choice == "3":
            print_comparison_table()
        elif choice == "4":
            print_discussion()
        elif choice == "0":
            break
        else:
            print("Invalid option.")