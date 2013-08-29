# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:28:04 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy.fft import rfft,irfft
from numpy import linspace

def f(t):	

	if trunc(2*t) % 2==0:
		return 1
	else:
		return -1
		
n = linspace(0,1,1000)
y = map(f,n)
c = rfft(y)
c[10:]=0
yt = irfft(c)
plot(y)
plot(yt)