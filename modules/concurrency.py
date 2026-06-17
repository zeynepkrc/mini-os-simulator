import threading
import time


def unsafe_increment(shared_data, iterations):
    for _ in range(iterations):
        temp = shared_data["counter"]
        time.sleep(0.00001)
        shared_data["counter"] = temp + 1


def safe_increment(shared_data, iterations, lock):
    for _ in range(iterations):
        with lock:
            temp = shared_data["counter"]
            time.sleep(0.00001)
            shared_data["counter"] = temp + 1


def run_race_condition_demo(thread_count, iterations):
    shared_data = {"counter": 0}
    threads = []

    print("\n===== Race Condition Demo =====")
    print("Multiple threads increment the same shared counter without synchronization.")

    for i in range(thread_count):
        thread = threading.Thread(
            target=unsafe_increment,
            args=(shared_data, iterations)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected_result = thread_count * iterations
    actual_result = shared_data["counter"]

    print(f"Thread Count: {thread_count}")
    print(f"Iterations per Thread: {iterations}")
    print(f"Expected Counter Value: {expected_result}")
    print(f"Actual Counter Value: {actual_result}")

    if actual_result != expected_result:
        print("Result: Race condition occurred. Some updates were lost.")
    else:
        print("Result: No visible race condition occurred in this run.")


def run_synchronization_demo(thread_count, iterations):
    shared_data = {"counter": 0}
    lock = threading.Lock()
    threads = []

    print("\n===== Correct Synchronization Demo =====")
    print("Multiple threads increment the same shared counter using a lock.")

    for i in range(thread_count):
        thread = threading.Thread(
            target=safe_increment,
            args=(shared_data, iterations, lock)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected_result = thread_count * iterations
    actual_result = shared_data["counter"]

    print(f"Thread Count: {thread_count}")
    print(f"Iterations per Thread: {iterations}")
    print(f"Expected Counter Value: {expected_result}")
    print(f"Actual Counter Value: {actual_result}")

    if actual_result == expected_result:
        print("Result: Synchronization successful. No updates were lost.")
    else:
        print("Result: Unexpected error. Counter value is incorrect.")


def run_demo():
    thread_count = 2
    iterations = 1000

    print("\n--- Concurrency Demo ---")
    print("This demo compares unsafe shared access and synchronized shared access.")

    run_race_condition_demo(thread_count, iterations)
    run_synchronization_demo(thread_count, iterations)


def run_custom_simulation():
    try:
        thread_count = int(input("Enter number of threads: "))
        iterations = int(input("Enter iterations per thread: "))

        if thread_count <= 0 or iterations <= 0:
            print("Thread count and iterations must be greater than zero.")
            return

        run_race_condition_demo(thread_count, iterations)
        run_synchronization_demo(thread_count, iterations)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_concurrency():
    while True:
        print("\n--- Concurrency Module ---")
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