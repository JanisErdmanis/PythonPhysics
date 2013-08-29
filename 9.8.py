# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:33:40 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from banded import banded
from pylab import *

h = 1e-18*10
hbar = 1.0546e-36
L = 1e-8
M = 9.109e-31
N = 1000 # Grid slices

a = L/N

a1 = 1 + h*hbar/2/M/a**2*1j
a2 = -h*hbar*1j/4/M/a**2
b1 =  1 - h*hbar/2/M/a**2*1j
b2 =  h*hbar*1j/4/M/a**2

ksi = zeros(N+1,complex)

def ksi0(x):
	x0 = L/2
	sigma = 1e-10
	k = 5e10
	return exp(-(x-x0)**2/2/sigma**2)*exp(1j*k*x)

x = linspace(0,L,N+1)
ksi[:] = ksi0(x)
ksi[[0,N]]=0


A = empty((3,N),complex)

A[0,:] = a2
A[1,:] = a1
A[2:,] = a2

#==============================================================================
# for i in range(100):
# 	v = b1*ksi[1:N] + b2*(ksi[2:N+1] + ksi[0:N-1])
# 	ksi[1:N] = banded(A,v,1,1)
#==============================================================================

#plot(ksi)

#==============================================================================
# Ap = zeros((N-1,N-1),complex)
# for i in range(N-2):
# 	Ap[i,i] = a2
# 	Ap[i+1,i] = a1 #Bottom
# 	Ap[i,i+1] = a1 #Right
# Ap[N-2,N-2] = a2
#==============================================================================


from visual import curve, rate

ksi_c = curve()
ksi_c.set_x(x-L/2)

#ksi = banded(A,v,1,1)
while True:
	rate(30)
	ksi_c.set_y(real(ksi)*1e-9)
	ksi_c.set_z(imag(ksi)*1e-9)	
	for i in range(20):
		v = b1*ksi[1:N] + b2*(ksi[2:N+1] + ksi[0:N-1])
		ksi[1:N] = banded(A,v,1,1)


#plot(ksi)
