# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:24:01 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *
from numpy import zeros
from cmath import exp

#E = empty((N,4),complex)
#E[:,3]=y

class	E_wrap:	
	def __init__(self,N):
		self.array = zeros((1 + log2(N),N),complex)
		self.N = N
	
	def __getitem__(self,(m,j,k)):
		
		k %= self.N/2**m # By using 7.45		
		return self.array[m,j+2**m*k]
		
	def __setitem__(self,(m,j,k),value):
		
		k %= self.N/2**m # By using 7.45		
		self.array[m,j+2**m*k]=value

def fft(y):
	N = len(y)
	E = E_wrap(N)
	E.array[-1,:]=y
	
	for m in range(int(log2(N))-1,-1,-1):
		for j in range(2**m):
			for k in range(N//2**m):
				E[m,j,k]=E[m+1,j,k]+exp(-2j*pi*k/(N/2**m))*E[m+1,j+2**m,k]
	return E.array[0,:]

y = loadtxt('cpresources/pitch.txt')
c = fft(y)
plot(abs(c))