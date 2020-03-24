# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
from math import sqrt
def fact(n):
	assert n >= 0, 'n doit être positif'
	result = int(n)
	i = 1
	while i < n :
		result = result*(n-i)
		i += 1

	return result		

def roots(a, b, c):

	d = b**2-4*a*c

	if d < 0 :
		a = ()
		
	elif d == 0 :
		root_1 = -b/(2*a)
		root_2 = b/(2*a)
		a = (root_1, root_2)
		
	else :
		root_1 = (-b+sqrt(d))/(2*a)
		root_2 = (-b-sqrt(d))/(2*a)
		

		a = (root_1, root_2)
	
	return a	


	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	pass

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(5, 6, -2))
	print(integrate('x ** 2 - 1', -1, 1))
