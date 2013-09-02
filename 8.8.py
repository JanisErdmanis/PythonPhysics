# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 22:08:48 2013

@author: akels
"""
from __future__ import division, print_function
from numpy import arange,empty, array
from pylab import *
from cmath import exp

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

def array_decorator(f,*args,**kwargs):	
	print('function decorated to return array')
	g = lambda *args,**kwargs: array(f(*args,**kwargs),float)
	return g


G = 1
M = 10
L = 2

@array_decorator
def f(r,t):
	
	x,y,vx,vy = r
	
	Dx = vx
	Dy = vy
	
	R = sqrt(x**2+y**2)
	a = - G*M/R/sqrt(R**2 + L**2/4)
	
	Dvx = a * x/R
	Dvy = a * y/R
	
	return [Dx,Dy,Dvx,Dvy]

#==============================================================================
# 
# @array_decorator
# def f(r,t):
# 	
# 	r,theta,r_d,theta_d = r
# 	
# 	Dr = r_d
# 	Dtheta = theta_d
# 	
# 	Dr_d = r*theta_d**2 - G*M/r/sqrt(r**2+L**2/4)
# 	Dtheta_d = - r_d/r*(1+theta_d)
# 	
# 	return Dr,Dtheta,Dr_d,Dtheta_d
#==============================================================================
	
prob = rksolve(f)
prob.initial_conditions = [1,0,0,1]
prob.iterate(0,10)

x = prob.solution[:,0]
y = prob.solution[:,1]

plot(x,y)
show()
#polar(theta,r)