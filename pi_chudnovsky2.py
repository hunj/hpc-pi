#Chudnovsky Algorithm                                                                                         
 
from decimal import *
from math import factorial, pi
import time

def compute_pi(n):
    cal_pi = Decimal(0)
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
compute_pi(2000)
