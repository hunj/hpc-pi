# Brent-Salamin (aka. Gauss-Legendre) Formula to approximation of Pi.
# uses Arithmetic-geometric mean.

from decimal import *
import datetime, time
import sys
import math

def main():
    # set up environment and announce
    calculated_pi = Decimal(0)
    a_n, b_n, t_next, p_next = Decimal(1), 1 / Decimal(math.sqrt(2)), Decimal(0.25), Decimal(1)

    print "Brent-Salamin's Method to Pi approximation, running for %s minutes..." % sys.argv[1]

    # set up and start timer
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))
    getcontext().prec = 10

    # the sweet part. constantly approximate Pi value.
    while True:
        # breaks when time's up
        if datetime.datetime.now() >= endTime:
            break
        getcontext().prec += 5


        a_next = Decimal((a_n + b_n) / 2)
        b_next = Decimal(math.sqrt(a_n * b_n))
        t_next -= Decimal(p_next) * Decimal((a_n - a_next) ** 2)
        p_next *= 2

        a_n = a_next
        b_n = b_next

        calculated_pi = Decimal((a_n + b_n) * (a_n + b_n)) / Decimal(4 * t_next)

    # time's up, finish up the calculation
    pi_decimal = Decimal(float(math.pi))

    # display cute message and quit.
    print "Calculated pi:", calculated_pi
    print "Difference to exact value of pi:", calculated_pi - pi_decimal
    print "Error: (approx-exact)/exact =", (calculated_pi - pi_decimal) / pi_decimal * 100, "%"


if __name__ == '__main__':
    main()
