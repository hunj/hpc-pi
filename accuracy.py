# Helper method

from math import pi

def accuracy_of_calculated_pi(computed_pi):
    diff = calculated_pi - math.pi
	print "Difference to exact value of pi: ", diff
	print "Error: (approx-exact)/exact =", diff / math.pi * 100, "%"