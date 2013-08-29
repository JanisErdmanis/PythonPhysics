# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:38:57 2013

@author: akels
"""
from __future__ import division, print_function

from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show

RC = 0.05

def V_in(t):
	
	if int(2*t)%2==0:
		return 1
	else:
		return -1

def f(x,t):
    return (V_in(t) - x)/RC

a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 0.0

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints)
xlabel("t")
ylabel("x(t)")
show()
