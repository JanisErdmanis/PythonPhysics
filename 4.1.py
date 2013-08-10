# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 13:38:04 2013

@author: akels
"""
from __future__ import division, print_function

print('Please give a integer value')
n = int(input())

#from math import factorial

def factorial(n):
	
	s = 1
	while n>1:
		s*=n
		n-=1
	return(s)
	
print('The factorial is {0}'.format(factorial(n)))