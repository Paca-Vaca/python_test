import time
import sys

import sequential
import threaded
import multiproc

if __name__ == "__main__":
    type = sys.argv[1]
    start = time.time()

    if type == 'sequential':
        sequential.sequential(80)
    elif type == 'threaded':
        threaded.threaded(80)
    elif type == 'threaded_delay':
        threaded.threaded_delay(80)
    elif type == 'multiproc':
        multiproc.multiproc(80) 

    end = time.time()
    print("took: ", end - start)
