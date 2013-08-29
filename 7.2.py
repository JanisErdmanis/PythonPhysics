# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:42:50 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *

data = loadtxt('cpresources/sunspots.txt',float)
y = data[:,1]
plot(y[500:1000])

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c
				
c = dft(y)
power = real(c)**2 + imag(c)**2
plot(power)