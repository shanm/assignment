import threading

# approach 1

def task():
    for _ in range(100000):
        pass

task1 = threading.Thread(target=task)
task2 = threading.Thread(target=task)

task1.start()
task2.start()

task1.join()
task2.join()

print("Both tasks completed")

###############################
# approach 2

def task(name):
    print(f"{name} started")

    for _ in range(100000):
        pass

    print(f"{name} completed")

task1 = threading.Thread(target=task, args=("Thread 1",))
task2 = threading.Thread(target=task, args=("Thread 2",))

task1.start()
task2.start()

task1.join()
task2.join()

print("All tasks completed")

########################

# Thread-safe example using a lock
import threading

counter = 0 # shared resource
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock: # Lock ensures only one thread modifies counter at a time.
            counter += 1

threads = []
for _ in range(5): # Create 5 threads
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

#print(threads)
for t in threads:
    t.join()

print(f"Final counter value: {counter}")

# Thread safe example using Queue
import threading
import queue

q = queue.Queue()

for _ in range(100000):
    q.put(1)

def process_queue():
    global counter
    while not q.empty():
        q.get()
        q.task_done()

threads = []
for _ in range(5):
    t = threading.Thread(target=process_queue)
    threads.append(t)
    t.start()
    
for t in threads:
    t.join()

print(f"Processing completed. Queue size: {q.qsize()}")

