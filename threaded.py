import threading

import heavy_fn

def threaded(n):
    threads = []

    for i in range(n):
        t = create_thread(heavy_fn.heavy, i, 500)
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def threaded_delay(n):
    threads = []
    for i in range(n):
        t = create_thread(heavy_fn.heavy_delay, i, 500)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# Utils functions
def create_thread(target, i, amount):
    return threading.Thread(target=target, args=(amount, i))