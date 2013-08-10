# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:01:32 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
#from pylab import *
from cmath import exp
from math import factorial,pi

f = lambda x: exp(2*x)
	
def derivative(fp,m,z0=0):
	
	f = lambda z: fp(z-z0)
#	m = 1
	N = 10000
	s = 0
	for k in range(N):
		z_k = exp(1j*2*pi*k/N)	
		s+=f(z_k)*exp(-1j*2*pi*k*m/N)
	
	I = s*factorial(m)/N
	return I

for m in range(10):
	s = derivative(f,m)
	print('m={}\t I={}'.format(m,s))