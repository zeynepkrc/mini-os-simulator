def simulate_raid_0(data_blocks, disk_count):
    disks = [[] for _ in range(disk_count)]

    print("\n===== RAID 0 Simulation =====")
    print("RAID 0 uses striping. Data blocks are distributed across disks.")

    for index, block in enumerate(data_blocks):
        disk_index = index % disk_count
        disks[disk_index].append(block)

    for i, disk in enumerate(disks):
        print(f"Disk {i + 1}: {disk}")

    total_blocks = len(data_blocks)
    usable_blocks = total_blocks

    print("\nRAID 0 Storage Usage")
    print("--------------------")
    print(f"Total Data Blocks: {total_blocks}")
    print(f"Usable Storage Blocks: {usable_blocks}")
    print("Storage Efficiency: 100%")

    print("\nRAID 0 Fault Tolerance")
    print("----------------------")
    print("Fault Tolerance: No")
    print("If one disk fails, some data blocks are lost and the whole data becomes incomplete.")

    return disks


def simulate_raid_1(data_blocks, disk_count):
    disks = []

    print("\n===== RAID 1 Simulation =====")
    print("RAID 1 uses mirroring. The same data is copied to every disk.")

    for _ in range(disk_count):
        disks.append(data_blocks.copy())

    for i, disk in enumerate(disks):
        print(f"Disk {i + 1}: {disk}")

    total_physical_blocks = len(data_blocks) * disk_count
    usable_blocks = len(data_blocks)
    efficiency = usable_blocks / total_physical_blocks

    print("\nRAID 1 Storage Usage")
    print("--------------------")
    print(f"Data Blocks: {len(data_blocks)}")
    print(f"Physical Storage Blocks Used: {total_physical_blocks}")
    print(f"Usable Storage Blocks: {usable_blocks}")
    print(f"Storage Efficiency: {efficiency * 100:.2f}%")

    print("\nRAID 1 Fault Tolerance")
    print("----------------------")
    print("Fault Tolerance: Yes")
    print("The system can continue working if one disk fails, because the other disk has a full copy.")

    return disks


def simulate_disk_failure_raid_0(disks, failed_disk_index):
    print("\n===== RAID 0 Disk Failure Simulation =====")

    if failed_disk_index < 0 or failed_disk_index >= len(disks):
        print("Invalid disk number.")
        return

    print(f"Disk {failed_disk_index + 1} failed.")
    print(f"Lost Blocks: {disks[failed_disk_index]}")
    print("Result: Data cannot be fully recovered in RAID 0.")


def simulate_disk_failure_raid_1(disks, failed_disk_index):
    print("\n===== RAID 1 Disk Failure Simulation =====")

    if failed_disk_index < 0 or failed_disk_index >= len(disks):
        print("Invalid disk number.")
        return

    print(f"Disk {failed_disk_index + 1} failed.")

    remaining_disks = [
        disk for index, disk in enumerate(disks)
        if index != failed_disk_index
    ]

    if remaining_disks:
        print(f"Recovered Data from Remaining Disk: {remaining_disks[0]}")
        print("Result: Data is still available in RAID 1.")
    else:
        print("Result: No remaining disk available.")


def run_demo():
    data_blocks = ["A", "B", "C", "D", "E", "F"]
    disk_count = 2

    print("\n--- RAID Demo ---")
    print(f"Data Blocks: {data_blocks}")
    print(f"Number of Disks: {disk_count}")

    raid_0_disks = simulate_raid_0(data_blocks, disk_count)
    simulate_disk_failure_raid_0(raid_0_disks, failed_disk_index=0)

    raid_1_disks = simulate_raid_1(data_blocks, disk_count)
    simulate_disk_failure_raid_1(raid_1_disks, failed_disk_index=0)


def run_custom_simulation():
    try:
        user_input = input("Enter data blocks separated by spaces: ")
        data_blocks = user_input.split()

        disk_count = int(input("Enter number of disks: "))

        if len(data_blocks) == 0:
            print("Data blocks cannot be empty.")
            return

        if disk_count < 2:
            print("At least 2 disks are required for this RAID simulation.")
            return

        raid_0_disks = simulate_raid_0(data_blocks, disk_count)

        failed_disk = int(input("\nEnter failed disk number for RAID 0 simulation: "))
        simulate_disk_failure_raid_0(raid_0_disks, failed_disk - 1)

        raid_1_disks = simulate_raid_1(data_blocks, disk_count)

        failed_disk = int(input("\nEnter failed disk number for RAID 1 simulation: "))
        simulate_disk_failure_raid_1(raid_1_disks, failed_disk - 1)

    except ValueError:
        print("Invalid input. Please enter numeric values where required.")


def run_raid():
    while True:
        print("\n--- RAID Module ---")
        print("1. Run demo")
        print("2. Enter custom simulation")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            run_demo()
        elif choice == "2":
            run_custom_simulation()
        elif choice == "0":
            break
        else:
            print("Invalid option.")