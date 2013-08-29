# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:51:42 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

class rksolve:
	
	def __init__(self,f):
		self.f = f
		self.initial_conditions = None
		self.solution = None
		
	def iterate(self,a,b,N=1000):
		
		f = self.f
		r0 = array(self.initial_conditions,float)
		
		h = (b-a)/N
		
		tpoints = arange(a,b,h)
		solution = empty(tpoints.shape + r0.shape,float)
		
		#r_points[0] = r0
		r = r0
		for i,t in enumerate(tpoints):
		    solution[i]=r
		    k1 = h*f(r,t)
		    k2 = h*f(r+0.5*k1,t+0.5*h)
		    k3 = h*f(r+0.5*k2,t+0.5*h)
		    k4 = h*f(r+k3,t+h)
		    r += (k1+2*k2+2*k3+k4)/6
		
		self.h = h
		self.solution = solution
		self.t = tpoints

l = 0.4
g = 9.81
m = 1

def f(r,t):
	
	teta1,teta2,omega1,omega2 = r
	
	Dteta1 = omega1
	Dteta2 = omega2
	
	Domega1 = -(omega1**2*sin(2*teta1 - 2*teta2) +\
			 2*omega2**2*sin(teta1 - teta2) +\
			 g/l*(sin(teta1-2*teta2) + 3*sin(teta1)) ) \
				/(3 - cos(2*teta1 - 2*teta2)) 
	
	Domega2 = ( 4*omega1**2*sin(teta1-teta2)\
			+ omega2**2*sin(2*teta1-2*teta2) \
			+ 2*g/l*(sin(2*teta1 - teta2) - sin(teta2)))\
			/(3 - cos(2*teta1 - 2*teta2)) 
			
	return array([Dteta1,Dteta2,Domega1,Domega2],float96)
	
def Energy(r):
	teta1,teta2,omega1,omega2 = r
	V = -m*g*l*(2*cos(teta1) + cos(teta2))
	T = m*l**2*(omega1**2 + 1./2*omega2**2 + omega1*omega2*cos(teta1 - teta2))
	
	return T + V
	
prob = rksolve(f)
prob.initial_conditions = [pi/2,pi/2,0,0]
prob.iterate(0,100,N=1e5)

teta1 = prob.solution[:,0]
teta2 = prob.solution[:,1]

plot(teta1)
plot(teta2)
show()

E = [Energy(ri) for ri in prob.solution]
plot(E)

from numpy import save
save('F8.1',prob.solution)
