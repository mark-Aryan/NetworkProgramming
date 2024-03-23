"""
Threading in Python is a technique that allows multiple tasks to run concurrently within a single process.
This can be useful for improving the performance of your program,
as it allows multiple tasks to be executed simultaneously,
rather than having to wait for one task to finish before starting another.

When you are purchasing a laptop or PC, you found 'Multi-Threading', etc. Our Processor also have threading to perform,
several task simultaneously.
"""

import threading


# Creating threads
def create_threads(ip_list, function):
    threads = []

    for ip in ip_list:
        th = threading.Thread(target=function, args=(ip,))  # args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()
