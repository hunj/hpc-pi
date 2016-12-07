# Monte-Carlo Method for approximation of Pi               

import random
from decimal import *
import datetime, time
import sys
import math

def is_in_unit_circle(x,y):
    return(x**2 + y**2) <= 1

def main():
    iterations, num_hit, calculated_pi = Decimal(0), Decimal(0), Decimal(0)
    
    #expect number of correct digits
    #output of calculated pi would have 5 digits
    getcontext().prec = 5
    start_time = time.time()
    k = 0
    
    #argument is the number of iterations 
    for k in range(int(sys.argv[1])):
        iterations += 1
        random_x, random_y = Decimal(str(random.random())), Decimal(str(random.random()))
        if is_in_unit_circle(random_x, random_y):
            num_hit += 1
    elapsed_time = time.time() - start_time
    calculated_pi = Decimal(4) * Decimal(num_hit) / Decimal(iterations)
    print "Time elapsed:", elapsed_time
    print "Calulated pi:", calculated_pi

if __name__ == '__main__':
    main()
