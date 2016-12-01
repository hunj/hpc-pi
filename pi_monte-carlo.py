# Monte-Carlo Method for approximation of Pi.

import random, decimal
import datetime, time
import sys

def is_in_unit_circle(x, y):
    return (x ** 2 + y ** 2) <= 1

def main():
    num_hit, iterations = 0, 0
    endTime = datetime.datetime.now() + datetime.timedelta(minutes=int(sys.argv[1]))
    while True:
        if datetime.datetime.now() >= endTime:
            break
        iterations += 1
        random_x, random_y = decimal.Decimal(str(random.random())), decimal.Decimal(str(random.random()))
        if is_in_unit_circle(random_x, random_y):
            num_hit += 1
    print "pi: ", 4.0 * num_hit / iterations

if __name__ == '__main__':
    main()
