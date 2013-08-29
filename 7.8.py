# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:07:00 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *
from numpy import loadtxt
from numpy.fft import rfft2,irfft2

data = loadtxt('cpresources/blur.txt')
gray()
imshow(data)
show()

# Part B
sigma = 25
f = lambda x,y: exp(-(x**2+y**2)/2/sigma**2)
gaussian = zeros(data.shape,float)
for i in range(data.shape[0]):
	for j in range(data.shape[1]):
		gaussian[i,j]+=f(i,j)
		gaussian[-i,-j]+=f(i,j)
		gaussian[-i,j]+=f(i,j)
		gaussian[i,-j]+=f(i,j)
imshow(gaussian)

# Part C

bf = rfft2(data)
ff = rfft2(gaussian)

af[ff>1e-3] = bf[ff>1e-3]/ff[ff>1e-3]
af[ff<=1e-3] = bf[ff<=1e-3]

a = irfft2(af)
imshow(a)