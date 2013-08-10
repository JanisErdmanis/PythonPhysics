# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 13:19:02 2013

@author: akels
"""
from __future__ import division, print_function

def f(x):
    return x**4 - 2*x + 1


def integrate(f,a,b,N=20):
	
	h = (b-a)/N
	
	s = 0.5*f(a) + 0.5*f(b)
	for k in range(1,N):
	    s += f(a+k*h)
	
	return h*s

I1 = integrate(f,0,2,5)
I2 = integrate(f,0,2,10)

diference = abs(4.4-I2)
delta = 1/3*abs(I2-I1)

print(
"""
N=10	I = {}
N=20	I = {}
delta = {}
difference = {}
delta - diference = {}
""".format(I1,I2,delta,diference,delta-diference)
)