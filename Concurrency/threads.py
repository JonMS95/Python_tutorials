'''
Same as most of the programming languages out there, Python provides threading mechanisms,
so that each thread can execute different tasks in parallel.
It's worth mentioning that Python features a global interpreter lock (GIL) which prevents
more than a single thread from executing Python interpreter at a single time. However, it
was sorted out as of Python 3.13.
'''

import threading
import requests     # Install it with "pip install requests" if needed.
import time

# Just execute HTTP GET request on the given URL.
def fetchURL(url: str) -> None:
    print(f"Fetching URL: {url}")
    r = requests.get(url)
    print(f"Done (URL: {url}): {len(r.text)} bytes.")

# Run three threads, each executing the function above for a given URL.
def runThreads() -> None:
    urls = [
        "https://example.com/"          ,
        "https://httpbin.org/get"       ,
        "https://httpbin.org/delay/2"
    ]

    threads = []
    start = time.time() # Get starting time.

    for u in urls:
        t = threading.Thread(target=fetchURL, args=(u,))    # target: function to execute, args: input arguments (follow same format).
        t.start()                                           # Start thread.
        threads.append(t)                                   # Append thread to list so as to join it later.
    
    for t in threads:
        t.join()    # Wait for thread to join main thread (current).

    print(f"Total time: {time.time() - start}")

def main():
    runThreads()

if __name__ == "__main__":
    main()