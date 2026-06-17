class JournaledFileSystem:
    def __init__(self):
        self.files = {}
        self.journal = []

    def show_state(self):
        print("\nCurrent File System State")
        print("-------------------------")
        print(f"Files: {self.files}")
        print(f"Journal: {self.journal}")

    def create_file(self, file_name, content, simulate_crash=False):
        print(f"\nCreating file: {file_name}")

        self.journal.append({
            "operation": "CREATE",
            "file_name": file_name,
            "content": content,
            "status": "START"
        })

        print("Journal updated: START CREATE operation")

        if simulate_crash:
            print("Simulated crash occurred before file creation was committed.")
            return

        self.files[file_name] = content
        print(f"File created: {file_name}")

        self.journal.append({
            "operation": "CREATE",
            "file_name": file_name,
            "content": content,
            "status": "COMMIT"
        })

        print("Journal updated: COMMIT CREATE operation")

    def delete_file(self, file_name, simulate_crash=False):
        print(f"\nDeleting file: {file_name}")

        if file_name not in self.files:
            print("File not found.")
            return

        old_content = self.files[file_name]

        self.journal.append({
            "operation": "DELETE",
            "file_name": file_name,
            "content": old_content,
            "status": "START"
        })

        print("Journal updated: START DELETE operation")

        if simulate_crash:
            print("Simulated crash occurred before delete operation was committed.")
            return

        del self.files[file_name]
        print(f"File deleted: {file_name}")

        self.journal.append({
            "operation": "DELETE",
            "file_name": file_name,
            "content": old_content,
            "status": "COMMIT"
        })

        print("Journal updated: COMMIT DELETE operation")

    def recover(self):
        print("\n===== Recovery Process Started =====")

        completed_operations = set()

        for entry in self.journal:
            if entry["status"] == "COMMIT":
                operation_key = (entry["operation"], entry["file_name"])
                completed_operations.add(operation_key)

        for entry in self.journal:
            if entry["status"] == "START":
                operation_key = (entry["operation"], entry["file_name"])

                if operation_key not in completed_operations:
                    print(f"Incomplete operation found: {entry['operation']} {entry['file_name']}")

                    if entry["operation"] == "CREATE":
                        if entry["file_name"] in self.files:
                            del self.files[entry["file_name"]]
                            print(f"Rolled back incomplete CREATE for {entry['file_name']}")
                        else:
                            print(f"No file created. Nothing to roll back for {entry['file_name']}")

                    elif entry["operation"] == "DELETE":
                        self.files[entry["file_name"]] = entry["content"]
                        print(f"Restored file after incomplete DELETE: {entry['file_name']}")

        self.journal.clear()
        print("Journal cleared after recovery.")
        print("Recovery completed.")


def run_demo():
    fs = JournaledFileSystem()

    print("\n--- Crash Consistency Demo ---")
    print("This demo shows simple journaling and recovery after a simulated crash.")

    fs.create_file("notes.txt", "Operating systems notes")
    fs.show_state()

    fs.create_file("temp.txt", "Temporary data", simulate_crash=True)
    fs.show_state()

    fs.recover()
    fs.show_state()

    fs.delete_file("notes.txt", simulate_crash=True)
    fs.show_state()

    fs.recover()
    fs.show_state()

    fs.delete_file("notes.txt")
    fs.show_state()


def run_custom_simulation():
    fs = JournaledFileSystem()

    while True:
        print("\n--- Crash Consistency Operations ---")
        print("1. Create file")
        print("2. Create file with simulated crash")
        print("3. Delete file")
        print("4. Delete file with simulated crash")
        print("5. Recover")
        print("6. Show file system state")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            file_name = input("Enter file name: ")
            content = input("Enter file content: ")
            fs.create_file(file_name, content)

        elif choice == "2":
            file_name = input("Enter file name: ")
            content = input("Enter file content: ")
            fs.create_file(file_name, content, simulate_crash=True)

        elif choice == "3":
            file_name = input("Enter file name: ")
            fs.delete_file(file_name)

        elif choice == "4":
            file_name = input("Enter file name: ")
            fs.delete_file(file_name, simulate_crash=True)

        elif choice == "5":
            fs.recover()

        elif choice == "6":
            fs.show_state()

        elif choice == "0":
            break

        else:
            print("Invalid option.")


def run_crash_consistency():
    while True:
        print("\n--- Crash Consistency Module ---")
        print("1. Run demo")
        print("2. Enter custom crash consistency operations")
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