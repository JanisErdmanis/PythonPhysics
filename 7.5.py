# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:17:14 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy import loadtxt
from numpy.fft import rfft, irfft

data = loadtxt('cpresources/dow2.txt')
N = data.shape[0]

plot(data,label='original')

c = rfft(data)
c[N//100:]=0
y=irfft(c)
plot(y,label='90%')
legend()
show()

def dct(y):
	N = len(y)
	y2 = empty(2*N,float)
	for n in range(N):
		y2[n] = y[n]
		y2[2*N - n -1] = y[n]
	c = rfft(y2)
	phi = exp(1j*pi*arange(N)/N)
	return real(c[:N]*phi)
	
def idct(a):
    N = len(a)
    c = empty(N+1,complex)

    phi = exp(1j*pi*arange(N)/(2*N))
    c[:N] = phi*a
    c[N] = 0.0
    return irfft(c)[:N]

plot(data,label='original')

c = dct(data)
c[N//100:]=0
y=idct(c)
plot(y,label='90%')
legend()
show()