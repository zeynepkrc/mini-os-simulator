import threading
import time
import random
from collections import deque


class ThreadSafeQueue:
    def __init__(self):
        self.queue = deque()
        self.condition = threading.Condition()

    def enqueue(self, item, producer_id):
        with self.condition:
            self.queue.append(item)
            print(f"Producer {producer_id} enqueued: {item}")
            print(f"Queue State: {list(self.queue)}")

            self.condition.notify()

    def dequeue(self, consumer_id):
        with self.condition:
            while len(self.queue) == 0:
                print(f"Consumer {consumer_id} is waiting because queue is empty.")
                self.condition.wait()

            item = self.queue.popleft()
            print(f"Consumer {consumer_id} dequeued: {item}")
            print(f"Queue State: {list(self.queue)}")

            return item

    def size(self):
        with self.condition:
            return len(self.queue)


def producer_task(queue, producer_id, item_count):
    for i in range(item_count):
        item = f"P{producer_id}-Item{i + 1}"
        time.sleep(random.uniform(0.1, 0.3))
        queue.enqueue(item, producer_id)


def consumer_task(queue, consumer_id, item_count):
    for _ in range(item_count):
        time.sleep(random.uniform(0.1, 0.4))
        queue.dequeue(consumer_id)


def run_demo():
    producer_count = 2
    consumer_count = 2
    items_per_producer = 5

    total_items = producer_count * items_per_producer
    items_per_consumer = total_items // consumer_count

    queue = ThreadSafeQueue()
    threads = []

    print("\n--- Thread-safe Queue Demo ---")
    print("This demo shows a queue safely shared by multiple producer and consumer threads.")
    print(f"Producer Count: {producer_count}")
    print(f"Consumer Count: {consumer_count}")
    print(f"Items per Producer: {items_per_producer}")

    for producer_id in range(1, producer_count + 1):
        thread = threading.Thread(
            target=producer_task,
            args=(queue, producer_id, items_per_producer)
        )
        threads.append(thread)
        thread.start()

    for consumer_id in range(1, consumer_count + 1):
        thread = threading.Thread(
            target=consumer_task,
            args=(queue, consumer_id, items_per_consumer)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nSimulation completed.")
    print(f"Final Queue Size: {queue.size()}")


def run_custom_simulation():
    try:
        producer_count = int(input("Enter number of producers: "))
        consumer_count = int(input("Enter number of consumers: "))
        items_per_producer = int(input("Enter items per producer: "))

        if producer_count <= 0 or consumer_count <= 0 or items_per_producer <= 0:
            print("All values must be greater than zero.")
            return

        total_items = producer_count * items_per_producer

        if total_items % consumer_count != 0:
            print("For this simple simulation, total items must be divisible by consumer count.")
            print(f"Total items: {total_items}")
            print(f"Consumer count: {consumer_count}")
            return

        items_per_consumer = total_items // consumer_count

        queue = ThreadSafeQueue()
        threads = []

        print("\n--- Custom Thread-safe Queue Simulation ---")

        for producer_id in range(1, producer_count + 1):
            thread = threading.Thread(
                target=producer_task,
                args=(queue, producer_id, items_per_producer)
            )
            threads.append(thread)
            thread.start()

        for consumer_id in range(1, consumer_count + 1):
            thread = threading.Thread(
                target=consumer_task,
                args=(queue, consumer_id, items_per_consumer)
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print("\nSimulation completed.")
        print(f"Final Queue Size: {queue.size()}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")


def run_thread_safe_queue():
    while True:
        print("\n--- Concurrent Data Structures Module ---")
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