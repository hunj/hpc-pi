# Monte-Carlo Method for approximation of Pi.

import random
from decimal import *
import datetime, time
import sys
import math

# checks whether given x, y coordinate is inside unit circle boundary.
# input:
#   - x: the x-coordinate of the point
#   - y: the y-coordinate of the point
# output: Boolean whether this point is inside the unit circle boundary.
def is_in_unit_circle(x, y):
    return (x ** 2 + y ** 2) <= 1

def main():
    # set up environment and announce
    print "Monte-Carlo method to Pi approximation, running for %s minutes..." % sys.argv[1]
    num_hit, iterations = Decimal(0), Decimal(0)

    # set up and start timer
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))
    getcontext().prec = 10

    # the sweet part. constantly approximate Pi value.
    while True:
        # breaks when time's up
        if datetime.datetime.now() >= endTime:
            break

        getcontext().prec += 5

        # monte-carlo method
        iterations += 1
        random_x, random_y = Decimal(str(random.random())), Decimal(str(random.random()))
        if is_in_unit_circle(random_x, random_y):
            num_hit += 1

    # multiply 4, since we are only on the first quadrant of the unit circle.
    calculated_pi = Decimal(4) * Decimal(num_hit) / Decimal(iterations)
    pi_decimal = Decimal(float(math.pi))
    # display cute message and quit.
    print "Calculated pi: ", calculated_pi
    print "Difference to exact value of pi: ", calculated_pi - pi_decimal
    print "Error: (approx-exact)/exact = ", (calculated_pi - pi_decimal) / pi_decimal * 100, "%"

if __name__ == '__main__':
    main()
