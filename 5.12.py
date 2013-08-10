# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 23:19:07 2013

@author: akels
"""

from __future__ import division, print_function
from math import factorial
from numpy import linspace,exp,sqrt,pi
from pylab import *


def H(n,x):
	H = [1,2*x]
	
	for ni in range(n):
		H.append(2*x*H[ni] - 2*ni*H[ni-1])
	
	return H[-1]

def ksi(n,x):
	
	return 1/sqrt(2**n*factorial(n)*sqrt(pi)) * exp(-x**2/2) * H(n,x)

	
x = linspace(-4,4)
n = [0,1,2,3]

for ni in n:
	plot(x,ksi(ni,x),label=ni)

legend()
show()

x = linspace(-10,10,200)
plot(x,ksi(30,x))
show()


#Integration

uncertainty = lambda n,x: x**2*ksi(n,x)**2

sys.path.append('cpresources')
from gaussxw import gaussxw

N = 100
x,w = gaussxw(N)

# 5.68
def x_sq(n):
	a = -1
	b = 1
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	
	y = (1 + xp**2)/(1-xp**2)**2*uncertainty(n,xp/(1-xp**2))
	s = sum(y*wp)
	return s

n = 5
#RMS = sqrt(sum([x_sq(ni)**2 for ni in range(1,n)]))
#print(RMS)
# 5.70
a = -pi/2
b = pi/2
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

n = 5
y = uncertainty(n,tan(xp))/cos(xp)**2
s = sum(y*wp)
print(s)

a = -10
b = 10
xp = 0.5*(b-a)*x + 0.5*(b+a)
wp = 0.5*(b-a)*w

n = 5
y = uncertainty(n,xp)
s = sum(y*wp)
print(s)