# Chudnovsky's Algorithm for approximation of Pi.

import math
from decimal import *
import time

def main():
    # set up environment and announce
    calculated_pi = Decimal(0)                          # the result
    load = Decimal(426880) * Decimal(math.sqrt(10005))  # the constant
    result = Decimal(0)                                 # the sum to be stored
    k = Decimal(0)                                      # iterator for summing

    print "Chudnovsky's Algorithm approach to Pi approximation, running for %s minutes..." % sys.argv[1]

    # set up and start timer
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))
    getcontext().prec = 10

    # the sweet part. constantly approximate Pi value.
    while True:
        # breaks when time's up
        if datetime.datetime.now() >= endTime:
            break

        getcontext().prec += 5

        numerator = factorial(6 * k) * (545140134 * k + 13591409)
        denominator = factorial(3 * k) * (factorial(k) ** Decimal(3))
        payload = Decimal(numerator) / Decimal(denominator)
        result += payload

    # time's up, finish up the calculation
    calculated_pi = load / result

    # display cute message and quit.
    print "Calculated pi: ", calculated_pi


if __name__ == '__main__':
    main()