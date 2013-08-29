# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 17:07:57 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy.random import *
#seed(1)
seed(5)

N = 20
J = 1
T = 1
kb = 1
beta = 1
steps = 100000#0000

s = empty((N,N),int)

for i in range(N):
	for j in range(N):
		if random()<0.5:
			s[i,j]=1
		else:
			s[i,j]=-1
			
def energy(s):
	
	s1 = s[:-1,:]*s[1:,:]
	s2 = s[:,:-1]*s[:,1:]
	
	E = -J*(sum(s1) + sum(s2))
	
	return E

def energy_check(s):
	
	I = 0
	for i in range(N-1):
		for j in range(N):
			I+=s[i,j]*s[i+1,j]
			
	for i in range(N):
		for j in range(N-1):
			I+=s[i,j]*s[i,j+1]
		
	return -J*I

eplot = []
Mplot = []
E1 = energy(s)
M = sum(s)
for k in range(steps):
	i = randint(N)
	j = randint(N)
	
	s[i,j] *=-1
	
	E2 = energy(s)
	
	dE = E2 - E1
	#print(dE)
	
	if dE>0:
		if random()<exp(-beta*dE):
			E1 = E2 #flip is acepted
			M = sum(s)
		else:
			s[i,j]*=-1
			#E1 = E2
	else:
		E1 = E2 #flip is accepted because energy falls
		M = sum(s)
		
	#eplot.append(E1)
	Mplot.append(M)
	
plot(Mplot)