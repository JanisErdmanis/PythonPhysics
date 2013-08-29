# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:59:45 2013

@author: akels
"""
from __future__ import division, print_function

from math import sin
from numpy import array,arange
from pylab import plot,xlabel,show

alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

def f(r,t):
    x = r[0]
    y = r[1]
    fx = alpha*x - beta*x*y
    fy = gamma*x*y-delta*y
    return array([fx,fy],float)

a = 0.0
b = 30.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []

r = array([2.0,2.0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plot(tpoints,xpoints,label='rabits')
plot(tpoints,ypoints,label='foxes')
xlabel("t")
ylabel('population in 1000')
legend()
show()

plot(xpoints,ypoints)
xlabel('rabits')
ylabel('foxes')
show()