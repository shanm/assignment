import multiprocessing

def worker(num):
    """Process worker function"""
    print(f'Worker: {num}')
    
if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()

    for p in jobs:
        p.join()

#################################################

import multiprocessing

def task(name):
    """Process worker function"""
    print(f"Worker {name}")


if __name__ == "__main__":

    processes = []

    for i in range(5):
        worker = multiprocessing.Process(
            target=task,
            args=(f"Name{i}",)
        )
        processes.append(worker)

    # Start all processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
