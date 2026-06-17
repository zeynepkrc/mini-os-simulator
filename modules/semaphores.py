import threading
import time
import random


class BoundedBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.capacity = capacity

        self.empty_slots = threading.Semaphore(capacity)
        self.full_slots = threading.Semaphore(0)
        self.mutex = threading.Lock()

    def produce(self, item, producer_id):
        self.empty_slots.acquire()

        with self.mutex:
            self.buffer.append(item)
            print(f"Producer {producer_id} produced item {item}")
            print(f"Buffer: {self.buffer}")

        self.full_slots.release()

    def consume(self, consumer_id):
        self.full_slots.acquire()

        with self.mutex:
            item = self.buffer.pop(0)
            print(f"Consumer {consumer_id} consumed item {item}")
            print(f"Buffer: {self.buffer}")

        self.empty_slots.release()
        return item


def producer_task(buffer, producer_id, item_count):
    for i in range(item_count):
        item = f"P{producer_id}-Item{i + 1}"
        time.sleep(random.uniform(0.1, 0.3))
        buffer.produce(item, producer_id)


def consumer_task(buffer, consumer_id, item_count):
    for _ in range(item_count):
        time.sleep(random.uniform(0.1, 0.4))
        buffer.consume(consumer_id)


def run_demo():
    buffer_capacity = 5
    producer_count = 2
    consumer_count = 2
    items_per_producer = 5

    total_items = producer_count * items_per_producer
    items_per_consumer = total_items // consumer_count

    buffer = BoundedBuffer(buffer_capacity)
    threads = []

    print("\n--- Producer-Consumer Demo Using Semaphores ---")
    print(f"Buffer Capacity: {buffer_capacity}")
    print(f"Producer Count: {producer_count}")
    print(f"Consumer Count: {consumer_count}")
    print(f"Items per Producer: {items_per_producer}")

    for producer_id in range(1, producer_count + 1):
        thread = threading.Thread(
            target=producer_task,
            args=(buffer, producer_id, items_per_producer)
        )
        threads.append(thread)
        thread.start()

    for consumer_id in range(1, consumer_count + 1):
        thread = threading.Thread(
            target=consumer_task,
            args=(buffer, consumer_id, items_per_consumer)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nSimulation completed.")
    print(f"Final Buffer State: {buffer.buffer}")


def run_custom_simulation():
    try:
        buffer_capacity = int(input("Enter buffer capacity: "))
        producer_count = int(input("Enter number of producers: "))
        consumer_count = int(input("Enter number of consumers: "))
        items_per_producer = int(input("Enter items per producer: "))

        if buffer_capacity <= 0 or producer_count <= 0 or consumer_count <= 0 or items_per_producer <= 0:
            print("All values must be greater than zero.")
            return

        total_items = producer_count * items_per_producer

        if total_items % consumer_count != 0:
            print("For this simple simulation, total items must be divisible by consumer count.")
            print(f"Total items: {total_items}")
            print(f"Consumer count: {consumer_count}")
            return

        items_per_consumer = total_items // consumer_count

        buffer = BoundedBuffer(buffer_capacity)
        threads = []

        print("\n--- Custom Producer-Consumer Simulation ---")

        for producer_id in range(1, producer_count + 1):
            thread = threading.Thread(
                target=producer_task,
                args=(buffer, producer_id, items_per_producer)
            )
            threads.append(thread)
            thread.start()

        for consumer_id in range(1, consumer_count + 1):
            thread = threading.Thread(
                target=consumer_task,
                args=(buffer, consumer_id, items_per_consumer)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("\nSimulation completed.")
        print(f"Final Buffer State: {buffer.buffer}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_semaphores():
    while True:
        print("\n--- Semaphores and Condition Variables Module ---")
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