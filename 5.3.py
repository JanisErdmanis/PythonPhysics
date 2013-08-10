# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:03:08 2013

@author: akels
"""
from __future__ import division, print_function
from numpy import *

f = lambda x: exp(-x**2)

def integrate(f,a,b):
	
	h = 0.1
	
	N = int((b-a)/h)
	
	
	delta = b-a - N*h

	I = 0
	
	if N>0:	
		s = (f(a) + f(b-delta))/2
		
		for k in range(1,N):
			s+= f(a+k*h)
	
		I = s*h

	I += 	delta*(f(b) + f(b-delta))/2
	
	return I

x = linspace(0,3)
E = [integrate(f,0,xi) for xi in x]

#E = integrate(f,0,x)

plot(x,E)
#plot(x,f(x))