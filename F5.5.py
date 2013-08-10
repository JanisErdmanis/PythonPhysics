# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:34:59 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *

from numpy import loadtxt

#data = loadtxt('cpresources/altitude.txt')
#h = 30000

data = loadtxt('cpresources/stm.txt')
h = 2.5

Nx,Ny = data.shape
f_x = empty((Nx,Ny))
f_y = empty((Nx,Ny))
I = empty((Nx,Ny))

Intensity = lambda w_x,w_y,fi=pi/4: (cos(fi)*w_x + sin(fi)*w_y)/ \
		sqrt(w_x**2 + w_y**2 +1)
		

for i in range(1,Nx-1):
	for j in range(1,Ny-1):
		f_x[i,j] = (data[i+1,j] - data[i-1,j])/2/h
		f_y[i,j] = (data[i,j+1] - data[i,j-1])/2/h		

		I[i,j] = Intensity(f_x[i,j],f_y[i,j],fi=pi/4)

gray()
imshow(I)

