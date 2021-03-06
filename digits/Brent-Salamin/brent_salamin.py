# Brent-Salamin's Method

from __future__ import with_statement
import decimal
import time

def pi_brent_salamin():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2 
        #the initial variables
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                
        pi = None
        start_time = time.time()
        #changing variables based on geometric sum
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            piold = pi
            pi    = (a + b) * (a + b) / (4 * t)

            #if calculated pi is not changing, then the limited precision has been reached so break
            if pi == piold:
                break
        elapsed_time = time.time() - start_time
        print elapsed_time
        return +pi

#the correct digits of pi to output
decimal.getcontext().prec = 100000
print pi_brent_salamin()
