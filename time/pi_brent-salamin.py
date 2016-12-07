# Brent-Salamin (aka. Gauss-Legendre) Formula to approximation of Pi.
# uses Arithmetic-geometric mean.

from decimal import *
from math import factorial, pi
import time

def main():
    # set up environment and announce
    calculated_pi = Decimal(0)
    num = Decimal(0)
    den = Decimal(0)
    getcontext().prec = 25000

    start_time = time.time()
    k = 0
    for k in range(n):
        num = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        den = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        cal_pi += Decimal(num)/Decimal(den)
    cal_pi = (Decimal(640320**(Decimal(3)/Decimal(2)))/Decimal(12))/Decimal(cal_pi)
    elapsed_time = time.time() - start_time
    print elapsed_time
    print cal_pi


def pi_brent_salamin():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        a, b, t, p = 1, 1/D(math.sqrt(2)), 1/D(4), 1                
        pi = None
        start_time = time.time()
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            piold = pi
            pi    = (a + b) * (a + b) / (4 * t)
            if pi == piold:
                break
        elapsed_time = time.time() - start_time
        print elapsed_time
        return +pi

decimal.getcontext().prec = 100000
print brent_salamin()
