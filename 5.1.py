# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 17:30:18 2013

@author: akels
"""

#def f(x):
#    return x**4 - 2*x + 1

from numpy import loadtxt, empty
from pylab import plot
data = loadtxt('cpresources/velocities.txt')

t,v = data[:,0],data[:,1]

h = 1
N = len(t)

#s = 0.5*v[0] #+ 0.5*v[-1]
distance = empty(N)
distance[0] = 0
for k in range(1,N):
	distance[k] = distance[k-1] + (v[k] + v[k-1])/2
	
plot(t,distance,label='distance')
plot(t,v,label='velocity')
legend()
#print(s*h)
