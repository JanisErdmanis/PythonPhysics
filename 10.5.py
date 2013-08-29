# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 12:13:42 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy.random import random
def f(x):
	return sin(1/x/(2-x))**2
	
a = 0
b = 2
A = (b-a)*1
N = 100000

x = random(N)*2
y = random(N)

fx = f(x)
count = sum(fx>y)
I1 = A*count/N
sigma1 = sqrt(I1*(A-I1)/N)
print('I1={0} + {1:5f}'.format(I1,sigma1))

I2 = (b-a)/N*sum(fx)
var2 = sum(fx**2)/N - (sum(fx)/N)**2
sigma2 = (b-a)*sqrt(var2/N)
print('I2={0} + {1:5f}'.format(I2,sigma2))
 