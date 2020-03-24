# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

from math import sqrt
from scipy.integrate import quad

def fact(n):
	if n == 0 :
		return 1
	else :
		assert n > 0, 'Negative Value'
		result = int(n)
		i = 1
		while i < n :
			result = result*(n-i)
			i += 1

		return result		

def roots(a, b, c):

	delta = b**2-4*a*c

	if delta < 0 :
		roots = ()
		
	elif delta == 0 :
		root_1 = -b/(2*a)
		roots = (root_1)
		
	else :
		root_1 = (-b+sqrt(delta))/(2*a)
		root_2 = (-b-sqrt(delta))/(2*a)
		

		roots = (root_1, root_2)
	
	return roots	

def integrate(function, lower, upper):

	def f(x) :
		return eval(function)
	result = quad(f, lower, upper)
	result = result[0]
	return int(result)


if __name__ == '__main__':
	print(fact(5))
	print(roots(1, -4, 4))
	print(integrate('x ** 2 - 1', -1, 1))
	print(integrate('2*x', -4, 2))
