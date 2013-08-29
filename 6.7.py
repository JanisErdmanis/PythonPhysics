# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:07:56 2013

@author: akels
"""
#from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
#from pylab import *
from math import pi
from numpy import empty,sin,arange, linspace
from numpy.linalg import eigvalsh, eigh

L = 5e-10
hbar = 1.0546e-34
M = 9.1094e-31
q = 1.6022e-19
a = 10*q


def H(m,n):
	
	s = 0
	#m+=1
	#n+=1
	if m==n:
		s+= ((hbar*pi*n)**2)/8/M + a/2*L**2/4
	
	if (m+n)%2==1:
		s+= -(2*L/pi)**2 * m*n/(m**2 - n**2)**2 * a/2
	
	return s
	
def Hp(m,n):
	
	s=0
	
	if m==n:
		s+= hbar**2/8/M*pi**2*n**2
	
	def I(m,n):
		
		if m==n:
			return L**2/4
		elif (m+n)%2 == 1:
			return -(2*L/pi)**2* m*n/(m**2-n**2)**2
		else:
			return 0
	
	s += a/2*I(m,n)
	return s

# Calculating the matrix
N = 100
A = empty((N,N),float)
for i in range(N):
	for j in range(N):
		A[i,j] = Hp(i+1,j+1)
		
X,ksi = eigh(A)
print(X[:10])

def wavefunction(x,m=1):
	n = arange(1,N+1)
	s = sum(ksi[:,m]*sin(pi*n*x/L))
	return s**2

x = linspace(0,L,100)

for i in range(3):
	ksi_i = [wavefunction(xi,m=i) for xi in x]
	plot(x,ksi_i,label=i)
legend()