import threading
import time


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def unsafe_withdraw(self, amount):
        if self.balance >= amount:
            current_balance = self.balance
            time.sleep(0.0001)
            self.balance = current_balance - amount

    def safe_withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                current_balance = self.balance
                time.sleep(0.0001)
                self.balance = current_balance - amount


def run_without_lock(initial_balance, thread_count, withdraw_amount):
    account = BankAccount(initial_balance)
    threads = []

    print("\n===== Without Mutex Lock =====")
    print("Multiple threads access the shared balance without protection.")

    for _ in range(thread_count):
        thread = threading.Thread(
            target=account.unsafe_withdraw,
            args=(withdraw_amount,)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected_balance = initial_balance - (thread_count * withdraw_amount)

    print(f"Initial Balance: {initial_balance}")
    print(f"Thread Count: {thread_count}")
    print(f"Withdraw Amount per Thread: {withdraw_amount}")
    print(f"Expected Final Balance: {expected_balance}")
    print(f"Actual Final Balance: {account.balance}")

    if account.balance != expected_balance:
        print("Result: Race condition occurred. Shared balance was not protected.")
    else:
        print("Result: Final balance is correct in this run, but the code is still unsafe.")


def run_with_lock(initial_balance, thread_count, withdraw_amount):
    account = BankAccount(initial_balance)
    threads = []

    print("\n===== With Mutex Lock =====")
    print("Multiple threads access the shared balance using a mutex lock.")

    for _ in range(thread_count):
        thread = threading.Thread(
            target=account.safe_withdraw,
            args=(withdraw_amount,)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    expected_balance = initial_balance - (thread_count * withdraw_amount)

    print(f"Initial Balance: {initial_balance}")
    print(f"Thread Count: {thread_count}")
    print(f"Withdraw Amount per Thread: {withdraw_amount}")
    print(f"Expected Final Balance: {expected_balance}")
    print(f"Actual Final Balance: {account.balance}")

    if account.balance == expected_balance:
        print("Result: Mutex lock protected the shared balance successfully.")
    else:
        print("Result: Unexpected error. Final balance is incorrect.")


def run_demo():
    initial_balance = 1000
    thread_count = 5
    withdraw_amount = 100

    print("\n--- Locks Module Demo ---")
    print("This demo shows how a mutex lock protects a shared bank account balance.")

    run_without_lock(initial_balance, thread_count, withdraw_amount)
    run_with_lock(initial_balance, thread_count, withdraw_amount)


def run_custom_simulation():
    try:
        initial_balance = int(input("Enter initial balance: "))
        thread_count = int(input("Enter number of threads: "))
        withdraw_amount = int(input("Enter withdraw amount per thread: "))

        if initial_balance < 0 or thread_count <= 0 or withdraw_amount <= 0:
            print("Invalid values. Balance must be non-negative, and other values must be positive.")
            return

        if thread_count * withdraw_amount > initial_balance:
            print("Warning: Total requested withdrawal is greater than initial balance.")
            print("Some withdrawals may not be completed.")

        run_without_lock(initial_balance, thread_count, withdraw_amount)
        run_with_lock(initial_balance, thread_count, withdraw_amount)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_locks():
    while True:
        print("\n--- Locks Module ---")
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