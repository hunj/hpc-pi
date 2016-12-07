#Nilakantha Series to compute pi                                                                                            
from __future__ import with_statement
import decimal
import time

def pi_nilakanta():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        step, pi, j = 0, D(3), D(2)
        start_time = time.time()
        while 1:
            piold = pi
            step += 1
            if step % 2 == 1:
                pi += D(4)/(j * (j + 1) * (j + 2))
            else:
                pi -= D(4)/(j * (j + 1) * (j + 2))
            j += 2

            #if the calculated pi is not changing b/c it has reached the limited precision, break                          
            if piold == pi:
                break
        elapsed_time = time.time() - start_time
        print "Time elapsed:", elapsed_time
        return +pi

#number of correct digits of pi to expect                                                                                   
decimal.getcontext().prec = 100
print pi_nilakanta()
