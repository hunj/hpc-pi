# Monte-Carlo Method for approximation of Pi.

import random
from decimal import *
import datetime, time
import sys
import math

def is_in_unit_circle(x, y):
    return (x ** 2 + y ** 2) <= 1

def main():
    print("Monte-Carlo method to Pi approximation...")
    num_hit, iterations = Decimal(0), Decimal(0)
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))
    while True:
        if datetime.datetime.now() >= endTime:
            break
        iterations += 1
        random_x, random_y = Decimal(str(random.random())), Decimal(str(random.random()))
        if is_in_unit_circle(random_x, random_y):
            num_hit += 1
    calculated_pi = Decimal(4) * Decimal(num_hit) / Decimal(iterations)
    print "Calculated pi: ", calculated_pi
    print "Difference to exact value of pi: ", calculated_pi - math.pi
    print "Error: (approx-exact)/exact = ", (calculated_pi - math.pi) / math.pi * 100, "%"

if __name__ == '__main__':
    main()
