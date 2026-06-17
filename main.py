from modules.process_management import run_process_management
from modules.cpu_scheduling import run_cpu_scheduling
from modules.address_translation import run_address_translation
from modules.segmentation import run_segmentation
from modules.paging import run_paging
from modules.tlb import run_tlb
from modules.page_replacement import run_page_replacement
from modules.concurrency import run_concurrency
from modules.locks import run_locks
from modules.semaphores import run_semaphores
from modules.thread_safe_queue import run_thread_safe_queue
from modules.disk_scheduling import run_disk_scheduling
from modules.raid import run_raid
from modules.file_system import run_file_system
from modules.crash_consistency import run_crash_consistency
from modules.ssd_hdd_analysis import run_ssd_hdd_analysis


def main():
    while True:
        print("\n===== MINI OPERATING SYSTEM SIMULATOR =====")
        print("1. Process Management")
        print("2. CPU Scheduling")
        print("3. Address Translation")
        print("4. Segmentation")
        print("5. Paging")
        print("6. TLB")
        print("7. Page Replacement")
        print("8. Concurrency")
        print("9. Locks")
        print("10. Semaphores and Condition Variables")
        print("11. Concurrent Data Structures")
        print("12. Disk Scheduling")
        print("13. RAID")
        print("14. File System")
        print("15. Crash Consistency")
        print("16. SSD vs HDD Analysis")
        print("0. Exit")

        choice = input("Select a module: ")

        if choice == "1":
            run_process_management()
        elif choice == "2":
            run_cpu_scheduling()
        elif choice == "3":
            run_address_translation()
        elif choice == "4":
            run_segmentation()
        elif choice == "5":
            run_paging()
        elif choice == "6":
            run_tlb()
        elif choice == "7":
            run_page_replacement()
        elif choice == "8":
            run_concurrency()
        elif choice == "9":
            run_locks()
        elif choice == "10":
            run_semaphores()
        elif choice == "11":
            run_thread_safe_queue()
        elif choice == "12":
            run_disk_scheduling()
        elif choice == "13":
            run_raid()
        elif choice == "14":
            run_file_system()
        elif choice == "15":
            run_crash_consistency()
        elif choice == "16":
            run_ssd_hdd_analysis()
        elif choice == "0":
            print("Exiting simulator...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()