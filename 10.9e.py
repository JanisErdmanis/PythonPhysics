# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:42:01 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *
from numpy.random import *
from visual import rate,sphere,color
seed(1)
#seed(5)

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

E1 = energy(s)
spin_repr = empty((N,N),sphere)
for i in range(N):
	for j in range(N):
		spin_repr[i,j]=sphere()
		spin_repr[i,j].pos = i-N//2,j-N//2,0
		
for k in range(steps):
	rate(500)
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
	else:
		E1 = E2 #flip is accepted because energy falls

	if s[i,j]==1:
		spin_repr[i,j].color = color.red
	else:
		spin_repr[i,j].color = color.green
	