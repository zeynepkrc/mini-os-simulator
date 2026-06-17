class Process:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.state = "NEW"
        self.program_counter = 0
        self.memory_limit = 1024

    def display_pcb(self):
        print("\nProcess Control Block")
        print("---------------------")
        print(f"PID: {self.pid}")
        print(f"Name: {self.name}")
        print(f"State: {self.state}")
        print(f"Priority: {self.priority}")
        print(f"Program Counter: {self.program_counter}")
        print(f"Memory Limit: {self.memory_limit} KB")


class ProcessManager:
    def __init__(self):
        self.processes = []
        self.next_pid = 1

    def create_process(self, name, priority):
        process = Process(self.next_pid, name, priority)
        self.processes.append(process)
        self.next_pid += 1

        print(f"\nProcess '{name}' created successfully.")
        process.display_pcb()

    def change_state(self, pid, new_state):
        for process in self.processes:
            if process.pid == pid:
                process.state = new_state
                print(f"\nProcess {pid} state changed to {new_state}.")
                process.display_pcb()
                return

        print("Process not found.")

    def terminate_process(self, pid):
        for process in self.processes:
            if process.pid == pid:
                process.state = "TERMINATED"
                print(f"\nProcess {pid} terminated.")
                process.display_pcb()
                self.processes.remove(process)
                return

        print("Process not found.")

    def list_processes(self):
        if not self.processes:
            print("\nNo active processes.")
            return

        print("\nActive Processes")
        print("----------------")
        for process in self.processes:
            print(
                f"PID: {process.pid}, "
                f"Name: {process.name}, "
                f"State: {process.state}, "
                f"Priority: {process.priority}"
            )


def run_process_management():
    manager = ProcessManager()

    while True:
        print("\n--- Process Management Module ---")
        print("1. Create process")
        print("2. Change process state")
        print("3. Terminate process")
        print("4. List processes")
        print("0. Back to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter process name: ")
            priority = int(input("Enter priority: "))
            manager.create_process(name, priority)

        elif choice == "2":
            pid = int(input("Enter PID: "))
            print("Available states: NEW, READY, RUNNING, WAITING, TERMINATED")
            new_state = input("Enter new state: ").upper()
            manager.change_state(pid, new_state)

        elif choice == "3":
            pid = int(input("Enter PID: "))
            manager.terminate_process(pid)

        elif choice == "4":
            manager.list_processes()

        elif choice == "0":
            break

        else:
            print("Invalid option.")