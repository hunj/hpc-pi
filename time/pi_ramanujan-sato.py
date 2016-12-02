# Ramanujan-Sato series approach for approximation of Pi.

import random
from decimal import *
import datetime, time
import sys
import math

def main():
    # set up environment and announce
    constant = Decimal(2 * math.sqrt(2)) / Decimal(99 ** 2) # the constant that is multiplied to the sum
    k = 0   # the iteration variable
    calculated_sum = Decimal(0)

    print "Ramanujan-Sato series approach to Pi approximation, running for %s minutes..." % sys.argv[1]

    # set up and start timer
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))

    # the sweet part. constantly approximate Pi value.
    while True:
        # breaks when time's up
        if datetime.datetime.now() >= endTime:
            break

        # Ramanujan-Sato series
        load_1 = math.factorial(4 * k) / (math.factorial(k) ** 4)
        load_2 = (26390 * k + 1103) / (396 ** (4 * k))

        calculated_sum += load_1 * load_2

    # time's up, finish up the calculation
    invert_pi = constant * calculated_sum
    calculated_pi = Decimal(invert_pi ** -1)

    # display cute message and quit.
    print "Calculated pi: ", calculated_pi
    print "Difference to exact value of pi: ", calculated_pi - math.pi
    print "Error: (approx-exact)/exact = ", (calculated_pi - math.pi) / math.pi * 100, "%"


if __name__ == '__main__':
    main()
