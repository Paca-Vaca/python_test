import multiprocessing

import heavy_fn

def multiproc(n):
    processes = []

    for i in range(n):
        p = multiprocessing.Process(target=heavy_fn.heavy, args=(i, 500))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()