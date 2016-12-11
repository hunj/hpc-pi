# Ramanu for approximation of Pi               

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
    
    #expect number of correct digits
    #output of calculated pi would have 5 digits
    getcontext().prec = 5
    start_time = time.time()
    
    #argument is the number of iterations 
    for k in range(int(sys.argv[1])):
        load_1 = math.factorial(4 * k) / (math.factorial(k) ** 4)
        load_2 = (26390 * k + 1103) / (396 ** (4 * k))

        k += 1
        calculated_sum += Decimal(load_1 * load_2)
    elapsed_time = time.time() - start_time

    # time's up, finish up the calculation
    invert_pi = constant * calculated_sum
    calculated_pi = Decimal(invert_pi ** -1)
    pi_decimal = Decimal(float(math.pi))

    print "Time elapsed:", elapsed_time
    print "Calulated pi:", calculated_pi


if __name__ == '__main__':
    main()



