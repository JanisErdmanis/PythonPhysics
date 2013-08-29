# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 13:35:52 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

A = 10
B = 12
tau = 365
D = 0.1
def T0(t):
	return A + B*sin(2*pi*t/tau)

L = 20     # Thickness of steel in meters
D = 0.1   # Thermal diffusivity
N = 100       # Number of divisions in grid
a = L/N       # Grid spacing
h = 0.01     # Time-step
#epsilon = h/1000

T = zeros(N+1,float)
T[1:N]=10


def iterate(T,t_min,t_max):
	# Main loop
	t = t_min
	c = h*D/a**2

	while t<t_max:
	
	    # Calculate the new values of T
		T[0] = T0(t)
		T[N] = 11
		T[1:N] = T[1:N] + c*(T[2:N+1]+T[0:N-1]-2*T[1:N])
	    
		#T,Tp = Tp,T
		t += h
	return T


T9 = iterate(T,0,365*9)

T9_i = T9
t_min = 365*9
for t_max in [365*9 + i*(365//4) for i in range(4)]:
	#t_max = t_min + 365//4
	T9_i = iterate(T9_i,t_min,t_max)
	plot(T9_i,label=t_max%365/(365//4))
	t_min = t_max

legend()
xlabel("x")
ylabel("T")
show()
