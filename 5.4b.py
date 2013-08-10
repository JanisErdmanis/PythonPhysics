# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 08:57:06 2013

@author: akels
"""

from __future__ import division, print_function

from numpy import cos,sin,pi,sqrt
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

x,y = mgrid[-1:1:100j,-1:1:100j]
r = sqrt(x**2 + y**2)
wavelength = 0.5
k = 2*pi/wavelength

I = (J(1,r*k)/k/r)**2
gray()
imshow(I,vmax=0.1/10,extent=(-1,1,-1,1))