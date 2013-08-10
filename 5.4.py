# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:36:30 2013

@author: akels
"""

from __future__ import division, print_function

from numpy import cos,sin,pi
from pylab import *

def J(m,x):	
	
	def f(teta):
	    return cos(m*teta - x*sin(teta))
	
	N = 1000
	a = 0.
	b = pi
	h = (b-a)/N
	
	s = f(a) + f(b) + 4*f(b-h)
	for k in range(1,N//2):
	    s += 4*f(a + (2*k-1)*h) + 2*f(a+2*k*h)
	
	I = h/3*s/pi
	
	return I

x = linspace(0,20)

plot(x,J(0,x),label='J0')
plot(x,J(1,x),label='J1')
plot(x,J(2,x),label='J2')
legend()