# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:11:24 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

N = 100
L_t = 10
h = L_t/N
g = 9.81

x = zeros(N+1,float)

x[0]=0
x[N]=0

delta = 1
while delta>1e-6:
	xp = h**2/g/2 + 1/2*(x[2:N+1] + x[0:N-1])
	delta = max(abs(xp-x[1:N]))
	x[1:N] = xp
	
plot(linspace(0,10,N+1),x)
xlabel('t')
ylabel('x')
show()