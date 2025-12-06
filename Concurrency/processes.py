'''
Processes solve Python threading's (GIL) issue since each process uses it's very own
Python interpreter issue. Commonly used for computationally heavy tasks. 
'''

from multiprocessing import Process
import time
import os

def processWork(n: int) -> None:
    print("PID: ", os.getpid(), " (Parent PID: ", os.getppid(), ") starts.")
    time.sleep(n)
    print("PID: ", os.getpid(), " (Parent PID: ", os.getppid(), ") ends.")

def main():
    processes = [Process(target=processWork, args=(i,)) for i in range(4)]

    for p in processes:
        p.start()
    
    for p in processes:
        p.join()

    print(f"All processes have joined main thread (PID: {os.getppid()})")

if __name__ == "__main__":
    main()