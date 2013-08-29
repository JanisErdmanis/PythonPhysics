# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 21:45:46 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy.fft import fft

d = 20e-6
alpha = pi/d
w = 200e-6
W = 10*w
wavelength = 500e-9
f = 1
q = lambda u: sin(alpha*u)**2

kmax = int(W*5e-2/wavelength)
x = wavelength*f/W*arange(200)

N = 1000
n = arange(N)
u = n*W/N - W/2
y = sqrt(q(u))
y[abs(u)>w/2]=0
c = fft(y)
I = (real(c)**2 + imag(c)**2)*W**2/N**2

plot(x*100,I[0:200])
xlabel('cm')
show()
imshow((I[:200],),aspect=40)