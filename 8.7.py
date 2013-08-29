# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:57:44 2013

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


def trajectory(m=1):
	ro = 1.22
	C = 0.47
	g = 9.81
	R = 8e-2
	
	@array_decorator
	def f(r,t):
		x,y,vx,vy = r
		
		v = sqrt(vx**2 + vy**2)
		F_fr = 1/2*pi*R**2*ro*C*v**2
		
		Dr = [vx,vy]
		
		Dvx = -F_fr/m*vx/v
		Dvy = -F_fr/m*vy/v - g
		Dv = [Dvx,Dvy]
		
		return Dr + Dv
	
	prob = rksolve(f)
	r0 = [0,0]
	v0e = 100*exp(1j*30/180*pi)
	v0 = [v0e.real,v0e.imag]
	prob.initial_conditions = r0 + v0
	prob.iterate(0,10)
	
	x = prob.solution[:,0]
	y = prob.solution[:,1]
	
	plot(x[y>0],y[y>0],label=m)
	
	return x[abs(y)<0.2][-1]



m_range = arange(0.5,5,0.05)
x_ground = [trajectory(m) for m in m_range]
legend()
show()

plot(m_range,x_ground)
xlabel('m')
ylabel('x')
show()
