# Nilakantha's series

from decimal import *
import math, time

def main():
    print("Monte-Carlo method to Pi approximation...")
    pi = Decimal(3)
    curr_multiplier = Decimal(2)
    iteration = Decimal(0)
    load = Decimal(1)

    while True:
        if datetime.datetime.now() >= endTime:
            break
        load = Decimal(4) / (curr_multiplier * (curr_multiplier+1) * (curr_multiplier+2))

        if iteration % 2 == 0:
            pi += load
        else:
            pi -= load
        curr_multiplier += 2
        iteration += 1
    print "pi: ", 4.0 * num_hit / iterations
    print "Calculated pi: ", calculated_pi
    print "Difference to exact value of pi: ", calculated_pi - math.pi
    print "Error: (approx-exact)/exact = ", (calculated_pi - math.pi) / math.pi * 100, "%"


if __name__ == '__main__':
    main()
compute_pi()