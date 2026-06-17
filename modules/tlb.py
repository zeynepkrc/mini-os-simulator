from collections import OrderedDict


def create_page_table():
    return {
        0: 3,
        1: 5,
        2: 7,
        3: 2,
        4: 9,
        5: 1,
    }


def print_page_table(page_table):
    print("\nPage Table")
    print("----------")
    print("Page Number\tFrame Number")

    for page_number, frame_number in page_table.items():
        print(f"{page_number}\t\t{frame_number}")


def print_tlb(tlb):
    print("\nCurrent TLB")
    print("-----------")

    if not tlb:
        print("TLB is empty.")
        return

    print("Page Number\tFrame Number")
    for page_number, frame_number in tlb.items():
        print(f"{page_number}\t\t{frame_number}")


def translate_with_tlb(page_table, tlb, virtual_address, page_size, tlb_capacity):
    print("\nTLB Address Translation")
    print("-----------------------")
    print(f"Virtual Address: {virtual_address}")

    if virtual_address < 0:
        print("Result: Invalid address. Virtual address cannot be negative.")
        return "invalid"

    page_number = virtual_address // page_size
    offset = virtual_address % page_size

    print(f"Page Number: {page_number}")
    print(f"Offset: {offset}")

    if page_number in tlb:
        frame_number = tlb[page_number]
        physical_address = frame_number * page_size + offset

        print("TLB Result: HIT")
        print(f"TLB Lookup: Page {page_number} -> Frame {frame_number}")
        print(f"Physical Address: {physical_address}")

        return "hit"

    print("TLB Result: MISS")
    print("The page was not found in the TLB. Checking page table...")

    if page_number not in page_table:
        print("Result: Page fault. Page is not found in the page table.")
        return "page_fault"

    frame_number = page_table[page_number]
    physical_address = frame_number * page_size + offset

    print(f"Page Table Lookup: Page {page_number} -> Frame {frame_number}")
    print(f"Physical Address: {physical_address}")

    if len(tlb) >= tlb_capacity:
        removed_page, removed_frame = tlb.popitem(last=False)
        print(f"TLB is full. Removed oldest entry: Page {removed_page} -> Frame {removed_frame}")

    tlb[page_number] = frame_number
    print(f"Added to TLB: Page {page_number} -> Frame {frame_number}")

    return "miss"


def run_demo():
    page_size = 100
    tlb_capacity = 3

    page_table = create_page_table()
    tlb = OrderedDict()

    virtual_addresses = [120, 250, 120, 370, 250, 499, 120, 650, 370, 250]

    total_accesses = 0
    hits = 0
    misses = 0
    page_faults = 0

    print("\n--- TLB Demo ---")
    print("The system first checks the TLB before checking the page table.")
    print(f"Page Size: {page_size}")
    print(f"TLB Capacity: {tlb_capacity}")

    print_page_table(page_table)

    for address in virtual_addresses:
        result = translate_with_tlb(page_table, tlb, address, page_size, tlb_capacity)

        if result == "hit":
            hits += 1
            total_accesses += 1
        elif result == "miss":
            misses += 1
            total_accesses += 1
        elif result == "page_fault":
            page_faults += 1
            total_accesses += 1

        print_tlb(tlb)

    hit_ratio = hits / total_accesses if total_accesses > 0 else 0

    print("\nTLB Statistics")
    print("--------------")
    print(f"Total Accesses: {total_accesses}")
    print(f"TLB Hits: {hits}")
    print(f"TLB Misses: {misses}")
    print(f"Page Faults: {page_faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}")
    print(f"Hit Ratio Percentage: {hit_ratio * 100:.2f}%")


def run_custom_translation():
    page_size = 100
    tlb_capacity = 3

    page_table = create_page_table()
    tlb = OrderedDict()

    total_accesses = 0
    hits = 0
    misses = 0
    page_faults = 0

    print_page_table(page_table)

    while True:
        user_input = input("\nEnter virtual address or 'q' to quit: ")

        if user_input.lower() == "q":
            break

        try:
            virtual_address = int(user_input)
            result = translate_with_tlb(page_table, tlb, virtual_address, page_size, tlb_capacity)

            if result == "hit":
                hits += 1
                total_accesses += 1
            elif result == "miss":
                misses += 1
                total_accesses += 1
            elif result == "page_fault":
                page_faults += 1
                total_accesses += 1

            print_tlb(tlb)

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    hit_ratio = hits / total_accesses if total_accesses > 0 else 0

    print("\nTLB Statistics")
    print("--------------")
    print(f"Total Accesses: {total_accesses}")
    print(f"TLB Hits: {hits}")
    print(f"TLB Misses: {misses}")
    print(f"Page Faults: {page_faults}")
    print(f"Hit Ratio: {hit_ratio:.2f}")
    print(f"Hit Ratio Percentage: {hit_ratio * 100:.2f}%")


def run_tlb():
    while True:
        print("\n--- TLB Module ---")
        print("1. Run demo")
        print("2. Enter custom virtual addresses")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            run_demo()
        elif choice == "2":
            run_custom_translation()
        elif choice == "0":
            break
        else:
            print("Invalid option.")