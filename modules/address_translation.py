def translate_address(virtual_address, base_register, limit_register):
    print("\nAddress Translation Process")
    print("---------------------------")
    print(f"Virtual Address: {virtual_address}")
    print(f"Base Register: {base_register}")
    print(f"Limit Register: {limit_register}")

    if virtual_address < 0:
        print("Result: Invalid address. Virtual address cannot be negative.")
        return None

    if virtual_address >= limit_register:
        print("Result: Invalid address. Address exceeds process memory limit.")
        return None

    physical_address = base_register + virtual_address

    print(f"Formula: Physical Address = Base Register + Virtual Address")
    print(f"Formula: Physical Address = {base_register} + {virtual_address}")
    print(f"Physical Address: {physical_address}")

    return physical_address


def run_demo():
    base_register = 1000
    limit_register = 500

    virtual_addresses = [120, 300, 499, 600]

    print("\n--- Address Translation Demo ---")
    print("A process is loaded into memory starting at physical address 1000.")
    print("The process is allowed to access virtual addresses from 0 to 499.")

    for address in virtual_addresses:
        translate_address(address, base_register, limit_register)


def run_custom_translation():
    try:
        base_register = int(input("Enter base register: "))
        limit_register = int(input("Enter limit register: "))
        virtual_address = int(input("Enter virtual address: "))

        translate_address(virtual_address, base_register, limit_register)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_address_translation():
    while True:
        print("\n--- Address Translation Module ---")
        print("1. Run demo")
        print("2. Enter custom address")
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