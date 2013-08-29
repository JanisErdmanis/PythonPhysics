# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:01:36 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

h = 2e-6
L = 1
v = 100

d = 0.1
C = 1
sigma = 0.3
N = 500 # grid spacings
a = L/N

def phi0(x):
	return C * x*(L-x)/L**2*exp(- (x-d)**2/2/sigma**2)
	
fi = zeros(N+1,float)

x = linspace(0,L,N+1)
phi = phi0(x)

#t = 0
#t_end = 50e-3/100

def iterate(fi,phi,dt=50e-3):
	iterations = int(dt/h)
	for i in range(iterations):
		fi[1:N] += h*phi[1:N]
		phi[1:N] += h*v**2/a**2*(fi[2:N+1] + fi[0:N-1] - 2*fi[1:N])
		#t +=h
	return fi,phi


#fi,phi = iterate(fi,phi,iterations = int(50e-3/h))
#plot(fi)
#show()

from visual import curve,rate

c = curve()
c.set_x(x - L/2)


while True:
	rate(30)	
	c.set_y(fi*2e3)
	fi,phi = iterate(fi,phi,dt = 50e-3/100)