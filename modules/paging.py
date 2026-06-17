def create_page_table():
    return {
        0: 3,
        1: 5,
        2: 7,
        3: 2,
        4: 9,
    }


def print_page_table(page_table):
    print("\nPage Table")
    print("----------")
    print("Page Number\tFrame Number")

    for page_number, frame_number in page_table.items():
        print(f"{page_number}\t\t{frame_number}")


def translate_virtual_address(page_table, virtual_address, page_size):
    print("\nPage Lookup and Address Translation")
    print("-----------------------------------")
    print(f"Virtual Address: {virtual_address}")
    print(f"Page Size: {page_size}")

    if virtual_address < 0:
        print("Result: Invalid address. Virtual address cannot be negative.")
        return None

    page_number = virtual_address // page_size
    offset = virtual_address % page_size

    print(f"Page Number = Virtual Address // Page Size = {virtual_address} // {page_size} = {page_number}")
    print(f"Offset = Virtual Address % Page Size = {virtual_address} % {page_size} = {offset}")

    if page_number not in page_table:
        print("Result: Page fault. Page is not found in the page table.")
        return None

    frame_number = page_table[page_number]
    physical_address = frame_number * page_size + offset

    print(f"Page Table Lookup: Page {page_number} -> Frame {frame_number}")
    print("Formula: Physical Address = Frame Number * Page Size + Offset")
    print(f"Formula: Physical Address = {frame_number} * {page_size} + {offset}")
    print(f"Physical Address: {physical_address}")

    return physical_address


def run_demo():
    page_size = 100
    page_table = create_page_table()

    print("\n--- Paging Demo ---")
    print("The virtual address is divided into page number and offset.")
    print("The page table maps page numbers to frame numbers.")

    print_page_table(page_table)

    virtual_addresses = [50, 120, 250, 370, 499, 650]

    for address in virtual_addresses:
        translate_virtual_address(page_table, address, page_size)


def run_custom_translation():
    page_size = 100
    page_table = create_page_table()

    print_page_table(page_table)

    try:
        virtual_address = int(input("\nEnter virtual address: "))
        translate_virtual_address(page_table, virtual_address, page_size)

    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def run_paging():
    while True:
        print("\n--- Paging Module ---")
        print("1. Run demo")
        print("2. Enter custom virtual address")
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