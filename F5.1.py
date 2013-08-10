# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 13:54:46 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *


f = lambda x,a=1: x**(a-1)*exp(-x)

a = [2,3,4]
x = linspace(0,5)

for ai in a:
	plot(x,f(x,ai),label=ai)
	
legend()
show()

def gamma(a):
	
	f = lambda x: exp((a-1)*log(x) -x)

	f_p = lambda z: f((a-1)*z/(1-z)) /(1-z)**2 
	
	N = 100
	h = 1/N
	s = 0.5*f_p(0) + 0.5*f_p(1- h/1000)
	for k in range(1,N):
		s += f_p(0+k*h)
	
	return h*s*(a-1)