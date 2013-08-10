# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 22:08:39 2013

@author: akels
"""


from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from gaussxw import gaussxw
from numpy import pi,exp,cos,tan

kb = 8.31/6.02e23
c = 3e8
h_ = 6.63e-34/2/pi

f = lambda x: x**3/(exp(x)-1)

N = 1000
h = (b-a)/N
a = 0 + h/1000
b = 1 - h/1000


f_ = lambda z: 1/(1-z)**2*f(z/(1-z))


s = 0.5*f_(a) + 0.5*f_(b)
for k in range(1,N):
    s += f_(a+k*h)

#s = sum(y*wp)

sigma = s*kb**4/4/pi**2/c**2/h_**3
print('sigma={}'.format(sigma))