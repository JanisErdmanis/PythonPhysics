# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:20:03 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy.random import random

N = 1000000
dim = 10

def f(x):
	
	r2 = zeros(x.shape[1],float)
	
	for xi in x:
		r2 += xi**2
	
	return r2<1


x = random((dim,N))*2 - 1

fx = f(x)
I = 2**dim/N * sum(fx)

var = sum(fx**2)/N-(sum(fx)/N)**2 
sigma = 2**dim*sqrt(var/N)
print('I = {} + {}'.format(I,sigma))

