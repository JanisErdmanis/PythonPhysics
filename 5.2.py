# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 18:13:12 2013

@author: akels
"""

def f(x):
    return x**4 - 2*x + 1

N = 10000
a = 0.0
b = 2.0
h = (b-a)/N

s = f(a) + f(b) + 4*f(b-h)
for k in range(1,N/2):
    s += 4*f(a + (2*k-1)*h) + 2*f(a+2*k*h)

#from math import abs
r = abs(h/3*s-4.4)/4.4

print('Value of the integral {} with releative error {}'.format(h/3*s,r))