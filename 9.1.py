# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 10:46:34 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *


# Constants
M = 100         # Grid squares on a side
V = 1.0         # Voltage at top wall
target = 1e-6   # Target accuracy
a = 0.01
epsilon0 = 8.85e-12

# Create arrays to hold potential values
phi = zeros([M+1,M+1],float)
#phi[0,:] = V
phiprime = zeros([M+1,M+1],float)

def ro(x,y):
	
	if x>0.6 and x<0.8 and y>0.6 and y<0.8:
		return 1
	elif x>0.2 and x<0.4 and y>0.2 and y<0.4:
		return -1
	else:
		return 0


# Main loop
delta = 1.0
while delta>target:

    # Calculate new values of the potential
    for i in range(1,M):
        for j in range(1,M):
           # if i==0 or i==M or j==0 or j==M:
            #    phiprime[i,j] = phi[i,j]
            #else:
            phiprime[i,j] = (phi[i+1,j] + phi[i-1,j] \
                                 + phi[i,j+1] + phi[i,j-1])/4 \
					+ a**2/4/epsilon0*ro(i*a,j*a)																												

    # Calculate maximum difference from old values
    delta = max(abs(phi-phiprime))

    # Swap the two arrays around
    phi,phiprime = phiprime,phi

# Make a plot
imshow(phi,origin='lower')
gray()
show()
