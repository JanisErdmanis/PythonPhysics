# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 11:08:57 2013

@author: akels
"""
from __future__ import division, print_function
from math import sin
from numpy import array,arange
from pylab import plot,xlabel,show


sigma_ = 10
r_=28
b_=8/3

def f(r,t):
    x = r[0]
    y = r[1]
    z = r[2]
    fx = sigma_*(y-x)
    fy = r_*x - y - x*z
    fz = x*y - b_*z
    return array([fx,fy,fz],float)

a = 0.0
b = 100.0
N = 10000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
ypoints = []
zpoints = []

r = array([0,1,0],float)
for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    zpoints.append(r[2])				
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

#plot(tpoints,xpoints)
plot(tpoints,ypoints)
xlabel("t")
show()

plot(zpoints,xpoints)
xlabel('x')
ylabel('z')
show()

