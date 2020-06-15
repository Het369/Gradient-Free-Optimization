#!/usr/bin/env python

import math

def f(x):
	'''
	Define the function that is to be minimised
	'''
	# ret = x*x + 9*x
	ret = -2*x*x + 21*x

	return ret

def fibonacci_search(a, b, epsilon):
	'''
	Update the interval based on golden section method
	Inputs: lower and upper limit of domain, epsilon
	Output: Optimal point 
	'''
	xl = a
	xu = b

	xp = xu - 0.618*(xu - xl)
	xq = xl + 0.618*(xu - xl)
	
	# Interval range length
	I = xu - xl

	# while(I > epsilon):
	# 	if(f(xp) <= f(xq)):
	# 		xu_new = xq 
	# 		xl_new = xl
	# 		I_new = xu_new - xl_new	
	# 		xq_new = xp
	# 		xp_new = xu_new - 0.618*I_new

	# 	else:
	# 		xl_new = xp
	# 		xu_new = xu
	# 		I_new = xu_new - xl_new
	# 		xp_new = xq
	# 		xq_new = xl_new + 0.618*I_new
		
		# update the variables
		xl = xl_new
		xu = xu_new
		xp = xp_new
		xq = xq_new
		I = I_new

	print 'The range is (', xl, ', ',  xu, ')'
	return ((xl+xu)/2.0) 

if __name__ == '__main__':
	'''
	a = lower limit of domain
	b = upper limit of domain
	epsilon = stopping criterion variable
	'''

	# a = -6
	# b = 6
	a = 1
	b = 9
	epsilon = 0.001
	
	x_star = fibonacci_search(a, b, epsilon)
	print 'The optimal point is', x_star

