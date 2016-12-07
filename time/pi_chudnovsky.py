# Chudnovsky's Algorithm for approximation of Pi.

from decimal import *
import datetime, time
import sys
import math

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

    pi_decimal = Decimal(float(math.pi))
    # display cute message and quit.
    print "Calculated pi: ", calculated_pi
    print "Difference to exact value of pi: ", calculated_pi - pi_decimal
    print "Error: (approx-exact)/exact = ", (calculated_pi - pi_decimal) / pi_decimal * 100, "%"

if __name__ == '__main__':
    main()