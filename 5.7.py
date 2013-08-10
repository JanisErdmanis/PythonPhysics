# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:35:39 2013

@author: akels
"""
from __future__ import division, print_function
from numpy import empty

def f(x):
    return sin(sqrt(100*x))**2

def resum(f,a,b,N):
	
	h = (b - a)/N
	
	s = 0
	for k in range(1,N//2+1):
		s+=f(a + (2*k-1)*h)
	
	return s*h
	
a = 0
b = 1


I = (b-a)/2*(f(b)+f(a))
eps=1
N=1

R = empty((100,100))
R[0,0]=I
i=0
while eps>1e-6:

	N*=2
	i+=1
	
	I_old = R[i-1,0]
	I_new = I_old/2 + resum(f,a,b,N)
	#eps = abs(I-I_new)/3
	#I = I_new
	
	R[i,0] = I_new
	s = '\t'
	s += '{0:.7f}'.format(R[i,0])
	for m in range(i):
		R[i,m+1] =R[i,m] + 1/(4**(m+1)-1)*(R[i,m] - R[i-1,m])
		s += ' {0:.7f}'.format(R[i,m])
	
	print(s)
	
	eps = abs(R[i,m+1]-R[i-1,m])
	#I = R[i,m+1]
	
	#print('N={}\t I={}\t eps={}'.format(N,I,eps))