# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:40:48 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
#from pylab import *
from math import pi
from numpy import exp
from gaussxw import gaussxw

wave1 = 390e-9
wave2 = 750e-9
c = 3e8
h = 1.0546e-34*2*pi
kb = 8.31/6.02e23

def fp(x):
    return x**3/(exp(x) - 1)

N = 100

# Calculate the sample points and weights, then map them
# to the required integration domain
x,w = gaussxw(N)

def mu(T):
	
	a = h*c/wave2/kb/T
	b = h*c/wave1/kb/T
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	
	# Perform the integration
	s = 0.0
	for k in range(N):
	    s += wp[k]*fp(xp[k])
	
	return s*15/pi**4
	
T = linspace(300,10000,100)
mu_list = map(mu,T)
plot(T,mu_list)

#Searching the root

accuracy = 1e-6         # Required accuracy in nm
z = (1+sqrt(5))/2       # Golden ratio

# Function to calculate the Buckingham potential
def f(T):
    return -mu(T)

# Initial positions of the four points
x1 = 300
x4 = 10000
x2 = x4 - (x4-x1)/z
x3 = x1 + (x4-x1)/z

# Initial values of the function at the four points
f1 = f(x1)
f2 = f(x2)
f3 = f(x3)
f4 = f(x4)

# Main loop of the search process
while x4-x1>accuracy:
    if f2<f3:
        x4,f4 = x3,f3
        x3,f3 = x2,f2
        x2 = x4 - (x4-x1)/z
        f2 = f(x2)
    else:
        x1,f1 = x2,f2
        x2,f2 = x3,f3
        x3 = x1 + (x4-x1)/z
        f3 = f(x3)

# Print the result
print("The maximum falls at",0.5*(x1+x4),"K")