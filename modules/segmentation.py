def create_segment_table():
    return {
        0: {"name": "Code", "base": 1000, "limit": 400},
        1: {"name": "Data", "base": 2000, "limit": 300},
        2: {"name": "Stack", "base": 3000, "limit": 500},
        3: {"name": "Heap", "base": 4000, "limit": 600},
    }


def print_segment_table(segment_table):
    print("\nSegment Table")
    print("-------------")
    print("Segment\tName\tBase\tLimit")

    for segment_number, segment in segment_table.items():
        print(
            f"{segment_number}\t"
            f"{segment['name']}\t"
            f"{segment['base']}\t"
            f"{segment['limit']}"
        )


def translate_logical_address(segment_table, segment_number, offset):
    print("\nLogical to Physical Address Translation")
    print("---------------------------------------")
    print(f"Logical Address: Segment {segment_number}, Offset {offset}")

    if segment_number not in segment_table:
        print("Result: Invalid segment number.")
        return None

    segment = segment_table[segment_number]
    base = segment["base"]
    limit = segment["limit"]

    print(f"Segment Name: {segment['name']}")
    print(f"Base Address: {base}")
    print(f"Segment Limit: {limit}")

    if offset < 0:
        print("Result: Invalid offset. Offset cannot be negative.")
        return None

    if offset >= limit:
        print("Result: Segmentation fault. Offset exceeds segment limit.")
        return None

    physical_address = base + offset

    print("Formula: Physical Address = Segment Base + Offset")
    print(f"Formula: Physical Address = {base} + {offset}")
    print(f"Physical Address: {physical_address}")

    return physical_address


def run_demo():
    segment_table = create_segment_table()

    print("\n--- Segmentation Demo ---")
    print_segment_table(segment_table)

    test_addresses = [
        (0, 120),
        (1, 250),
        (2, 480),
        (3, 700),
        (5, 100),
    ]

    for segment_number, offset in test_addresses:
        translate_logical_address(segment_table, segment_number, offset)


def run_custom_translation():
    segment_table = create_segment_table()
    print_segment_table(segment_table)

    try:
        segment_number = int(input("\nEnter segment number: "))
        offset = int(input("Enter offset: "))

        translate_logical_address(segment_table, segment_number, offset)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_segmentation():
    while True:
        print("\n--- Segmentation Module ---")
        print("1. Run demo")
        print("2. Enter custom logical address")
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