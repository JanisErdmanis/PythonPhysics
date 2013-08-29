# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:56:30 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *

c = 2
accuracy = 1e-6

x1 = 1.0
error = 1.0
iterations = 0

# Standart method
while error>accuracy:
	x1,x2 = 1 - exp(-c*x1), x1
	error = abs((x1-x2)/(1-1/(c*exp(-c*x1))))
	iterations+=1
	
print('The result is {} it took {} iterations'.format(x1,iterations))

# Overrelaxation
omega = -1
x1 = 1.0
error = 1.0
iterations = 0
while error>accuracy:
	x1,x2 = (1 - exp(-c*x1))*(1 + omega) - omega*x1, x1
	error = abs((x1-x2)/(1-1/(    (1 + omega)*(c*exp(-c*x1)) - omega  )))
	iterations+=1
	
print('The result is {} it took {} iterations'.format(x1,iterations))

# Loop until error is small enough
c_list = arange(0.01,3,0.1)
x_list = []

for c in c_list:	
	x1 = 1.0
	error = 1.0
	
	while error>accuracy:
		x1,x2 = 1 - exp(-c*x1), x1
		error = abs((x1-x2)/(1-1/(c*exp(-c*x1))))
	
	x_list.append(x1)
	
plot(x_list,c_list)
