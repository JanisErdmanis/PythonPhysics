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

data = loadtxt('cpresources/dow.txt')
N = data.shape[0]

plot(data,label='original')

c = rfft(data)
c[N//100:]=0
y=irfft(c)
plot(y,label='90%')
legend()
