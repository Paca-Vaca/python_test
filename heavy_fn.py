import time

def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    
    print(myid, "is done")

def heavy_delay(n, myid):
    time.sleep(2)
    print(myid, " is done")
