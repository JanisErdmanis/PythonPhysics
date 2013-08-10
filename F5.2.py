# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:19:31 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *
from cmath import exp

d = 20e-6
alpha = pi/d
q = lambda u: sin(alpha*u)**2

w = 10 * d
wavelength = 500e-9
focus = 1
k = 2*pi/wavelength


def I(x):
	
	f = lambda u,x: sqrt(q(u))*exp(1j*k*u * x/focus)
		
	N = 100
	a = -w/2
	b = w/2
	h = (b-a)/N
	
	s = 0.5*f(a,x) + 0.5*f(b,x)
	for i in range(1,N):
	    s += f(a+i*h,x)
	
	return  h**2 * (real(s)**2 + imag(s)**2)

x = linspace(-0.05,0.05,300)
intensity = [I(xi) for xi in x]

imshow([intensity],aspect=25)
