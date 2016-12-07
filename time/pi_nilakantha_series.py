# Nilakantha's series approach for approximation of Pi.

from decimal import *
import datetime, time
import math
import sys

def main():
    # set up environment and announce    
    calculated_pi = Decimal(3)
    curr_multiplier = Decimal(2)
    iteration = Decimal(0)
    load = Decimal(1)

    print "Monte-Carlo method to Pi approximation, running for %s minutes..." % sys.argv[1]

    # Set up and start timer
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))
    getcontext().prec = 10

    # the sweet part. constantly approximate Pi value.
    while True:
        # breaks when time's up
        if datetime.datetime.now() >= endTime:
            break

        getcontext().prec += 5

        # Nilakantha's series 
        load = Decimal(4) / (curr_multiplier * (curr_multiplier+1) * (curr_multiplier+2))
        if iteration % 2 == 0:
            calculated_pi += load
        else:
            calculated_pi -= load
        curr_multiplier += 2
        iteration += 1

    # time's up, finish up the calculation
    calculated_pi = 4.0 * num_hit / iterations

    # display cute message and quit.
    print "Calculated pi: ", calculated_pi
    print "Difference to exact value of pi: ", calculated_pi - math.pi
    print "Error: (approx-exact)/exact = ", (calculated_pi - math.pi) / math.pi * 100, "%"


if __name__ == '__main__':
    main()