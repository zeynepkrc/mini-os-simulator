class Directory:
    def __init__(self, name):
        self.name = name
        self.subdirectories = {}
        self.files = {}


class FileSystem:
    def __init__(self):
        self.root = Directory("/")

    def split_path(self, path):
        return [part for part in path.strip("/").split("/") if part]

    def find_directory(self, path):
        if path == "/":
            return self.root

        parts = self.split_path(path)
        current = self.root

        for part in parts:
            if part not in current.subdirectories:
                return None
            current = current.subdirectories[part]

        return current

    def create_directory(self, path):
        parts = self.split_path(path)

        if not parts:
            print("Root directory already exists.")
            return

        current = self.root

        for part in parts:
            if part not in current.subdirectories:
                current.subdirectories[part] = Directory(part)
                print(f"Directory created: {part}")
            current = current.subdirectories[part]

        print(f"Directory path ready: {path}")

    def create_file(self, directory_path, file_name, content):
        directory = self.find_directory(directory_path)

        if directory is None:
            print("Directory not found.")
            return

        if file_name in directory.files:
            print("File already exists. Overwriting file content.")

        directory.files[file_name] = content
        print(f"File created: {directory_path}/{file_name}")

    def delete_file(self, directory_path, file_name):
        directory = self.find_directory(directory_path)

        if directory is None:
            print("Directory not found.")
            return

        if file_name not in directory.files:
            print("File not found.")
            return

        del directory.files[file_name]
        print(f"File deleted: {directory_path}/{file_name}")

    def lookup_file(self, directory_path, file_name):
        directory = self.find_directory(directory_path)

        if directory is None:
            print("Directory not found.")
            return

        if file_name not in directory.files:
            print("File not found.")
            return

        print("\nFile Found")
        print("----------")
        print(f"Path: {directory_path}/{file_name}")
        print(f"Content: {directory.files[file_name]}")

    def list_directory(self, path):
        directory = self.find_directory(path)

        if directory is None:
            print("Directory not found.")
            return

        print(f"\nDirectory Listing: {path}")
        print("------------------")

        if not directory.subdirectories and not directory.files:
            print("Directory is empty.")
            return

        for directory_name in directory.subdirectories:
            print(f"[DIR]  {directory_name}")

        for file_name in directory.files:
            print(f"[FILE] {file_name}")

    def print_tree(self, directory=None, indent=""):
        if directory is None:
            directory = self.root
            print("\nFile System Tree")
            print("----------------")
            print("/")

        for directory_name, subdirectory in directory.subdirectories.items():
            print(f"{indent}├── {directory_name}/")
            self.print_tree(subdirectory, indent + "│   ")

        for file_name in directory.files:
            print(f"{indent}├── {file_name}")


def run_demo():
    fs = FileSystem()

    print("\n--- File System Demo ---")

    fs.create_directory("/home")
    fs.create_directory("/home/user")
    fs.create_directory("/docs")

    fs.create_file("/home/user", "notes.txt", "Operating systems notes")
    fs.create_file("/home/user", "project.py", "Mini OS Simulator code")
    fs.create_file("/docs", "report.docx", "Technical report draft")

    fs.list_directory("/")
    fs.list_directory("/home/user")

    fs.lookup_file("/home/user", "notes.txt")

    fs.delete_file("/home/user", "notes.txt")

    fs.lookup_file("/home/user", "notes.txt")

    fs.print_tree()


def run_custom_simulation():
    fs = FileSystem()

    while True:
        print("\n--- File System Operations ---")
        print("1. Create directory")
        print("2. Create file")
        print("3. Delete file")
        print("4. Lookup file")
        print("5. List directory")
        print("6. Print file system tree")
        print("0. Back")

        choice = input("Select an option: ")

        if choice == "1":
            path = input("Enter directory path, example /home/user: ")
            fs.create_directory(path)

        elif choice == "2":
            directory_path = input("Enter directory path: ")
            file_name = input("Enter file name: ")
            content = input("Enter file content: ")
            fs.create_file(directory_path, file_name, content)

        elif choice == "3":
            directory_path = input("Enter directory path: ")
            file_name = input("Enter file name: ")
            fs.delete_file(directory_path, file_name)

        elif choice == "4":
            directory_path = input("Enter directory path: ")
            file_name = input("Enter file name: ")
            fs.lookup_file(directory_path, file_name)

        elif choice == "5":
            path = input("Enter directory path: ")
            fs.list_directory(path)

        elif choice == "6":
            fs.print_tree()

        elif choice == "0":
            break

        else:
            print("Invalid option.")


def run_file_system():
    while True:
        print("\n--- File System Module ---")
        print("1. Run demo")
        print("2. Enter custom file system operations")
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