# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 20:29:10 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *
from numpy.random import random, standard_normal

Tmax = 1
Tmin = 1e-3
tau = 1e4
x0 = 2

def g(x):
	if x>0 and x<100:
		return cos(x) + cos(sqrt(2)*x + cos(sqrt(3)*x))
	else:
		return 1e10
	
def swap_function(f):	
	
	def h(x): return g(x)
	
	return h
	

@swap_function
def f(x):
	return x**2 - cos(4*pi*x)

fx = f(x0)
t = 0
T = Tmax
x = x0

while T>Tmin:
	
	t+=1
	T = Tmax*exp(-t/tau)
	
	oldx = x
	oldfx = fx
	r = standard_normal()
	x += r
	fx = f(x)
	
	delta_fx = fx - oldfx
	
	if random()>exp(-delta_fx/T):
		x = oldx
		fx = oldfx
		
print('x = {} with f(x) = {}'.format(x,fx))