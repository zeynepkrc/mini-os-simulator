from collections import deque


def print_frames(frames, frame_count):
    display = list(frames)

    while len(display) < frame_count:
        display.append("-")

    print("Frames:", display)


def fifo_page_replacement(reference_string, frame_count):
    print("\n===== FIFO Page Replacement =====")

    frames = deque()
    page_faults = 0
    page_hits = 0

    for page in reference_string:
        print(f"\nAccessing Page: {page}")

        if page in frames:
            page_hits += 1
            print("Result: Page Hit")
        else:
            page_faults += 1
            print("Result: Page Fault")

            if len(frames) >= frame_count:
                removed_page = frames.popleft()
                print(f"Removed Page: {removed_page}")

            frames.append(page)
            print(f"Added Page: {page}")

        print_frames(frames, frame_count)

    fault_rate = page_faults / len(reference_string)

    print("\nFIFO Summary")
    print("------------")
    print(f"Total References: {len(reference_string)}")
    print(f"Page Hits: {page_hits}")
    print(f"Page Faults: {page_faults}")
    print(f"Page Fault Rate: {fault_rate:.2f}")
    print(f"Page Fault Rate Percentage: {fault_rate * 100:.2f}%")

    return page_faults, fault_rate


def lru_page_replacement(reference_string, frame_count):
    print("\n===== LRU Page Replacement =====")

    frames = []
    page_faults = 0
    page_hits = 0

    for page in reference_string:
        print(f"\nAccessing Page: {page}")

        if page in frames:
            page_hits += 1
            print("Result: Page Hit")

            frames.remove(page)
            frames.append(page)
            print(f"Updated recent usage for Page: {page}")

        else:
            page_faults += 1
            print("Result: Page Fault")

            if len(frames) >= frame_count:
                removed_page = frames.pop(0)
                print(f"Removed Least Recently Used Page: {removed_page}")

            frames.append(page)
            print(f"Added Page: {page}")

        print_frames(frames, frame_count)

    fault_rate = page_faults / len(reference_string)

    print("\nLRU Summary")
    print("-----------")
    print(f"Total References: {len(reference_string)}")
    print(f"Page Hits: {page_hits}")
    print(f"Page Faults: {page_faults}")
    print(f"Page Fault Rate: {fault_rate:.2f}")
    print(f"Page Fault Rate Percentage: {fault_rate * 100:.2f}%")

    return page_faults, fault_rate


def compare_algorithms(fifo_result, lru_result):
    fifo_faults, fifo_rate = fifo_result
    lru_faults, lru_rate = lru_result

    print("\n===== Page Replacement Comparison =====")
    print("Algorithm\tPage Faults\tFault Rate")
    print(f"FIFO\t\t{fifo_faults}\t\t{fifo_rate:.2f}")
    print(f"LRU\t\t{lru_faults}\t\t{lru_rate:.2f}")

    if fifo_faults < lru_faults:
        print("\nFIFO performed better for this reference string.")
    elif lru_faults < fifo_faults:
        print("\nLRU performed better for this reference string.")
    else:
        print("\nBoth algorithms had the same number of page faults.")


def run_demo():
    reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frame_count = 3

    print("\n--- Page Replacement Demo ---")
    print(f"Reference String: {reference_string}")
    print(f"Frame Count: {frame_count}")

    fifo_result = fifo_page_replacement(reference_string, frame_count)
    lru_result = lru_page_replacement(reference_string, frame_count)

    compare_algorithms(fifo_result, lru_result)


def run_custom_simulation():
    try:
        user_input = input("Enter page reference string separated by spaces: ")
        reference_string = [int(page) for page in user_input.split()]

        frame_count = int(input("Enter number of frames: "))

        if frame_count <= 0:
            print("Frame count must be greater than zero.")
            return

        if len(reference_string) == 0:
            print("Reference string cannot be empty.")
            return

        fifo_result = fifo_page_replacement(reference_string, frame_count)
        lru_result = lru_page_replacement(reference_string, frame_count)

        compare_algorithms(fifo_result, lru_result)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_page_replacement():
    while True:
        print("\n--- Page Replacement Module ---")
        print("1. Run demo")
        print("2. Enter custom reference string")
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