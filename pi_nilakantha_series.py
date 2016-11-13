# Nilakantha's series

from decimal import *
import time

def compute_pi():
    pi = Decimal(3)
    curr_multiplier = Decimal(2)
    iteration = Decimal(0)
    load = Decimal(1)
    getcontext().prec = 6

    start_time = time.time()
    print start_time
    while iteration < Decimal(1000000000):
        load = Decimal(4) / (curr_multiplier * (curr_multiplier+1) * (curr_multiplier+2))

        if iteration % 2 == 0:
            pi += load
        else:
            pi -= load
        curr_multiplier += 2
        iteration += 1
        getcontext().prec += 1
    elapsed_time = time.time() - start_time
    print elapsed_time
    print pi

compute_pi()