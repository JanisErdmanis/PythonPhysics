# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:58:37 2013

@author: akels
"""
from __future__ import division, print_function
from numpy import arange,empty, array,sin
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
		
		self.solution = solution
		self.t = tpoints

omega = 1

def f(r,t):
    x = r[0]
    x_d = r[1]
    fx = x_d
    fx_d =  -omega**2*x
    return array([fx,fx_d],float)


prob = rksolve(f)
prob.initial_conditions=[1,0]
prob.iterate(0,50,N=50)
x = prob.solution[:,0]
plot(prob.t,x)

prob = rksolve(f)
prob.initial_conditions=[2,0]
prob.iterate(0,50,N=50)
x = prob.solution[:,0]
plot(prob.t,x,label='large amplitude')

legend()
xlabel("t")
show()

#Problem C

def f(r,t):
    x = r[0]
    x_d = r[1]
    fx = x_d
    fx_d =  -omega**2*x**3
    return array([fx,fx_d],float)


prob = rksolve(f)
prob.initial_conditions=[1,0]
prob.iterate(0,50,N=1000)
x = prob.solution[:,0]
plot(prob.t,x)

prob = rksolve(f)
prob.initial_conditions=[1.1,0]
prob.iterate(0,50,N=1000)
x = prob.solution[:,0]
plot(prob.t,x,label='large amplitude')

legend()
xlabel("t")
show()

# Part D
prob = rksolve(f)
prob.initial_conditions=[1,0]
prob.iterate(0,50,N=1000)
x = prob.solution[:,0]
x_d = prob.solution[:,1]
plot(x,x_d)

prob = rksolve(f)
prob.initial_conditions=[1.1,0]
prob.iterate(0,50,N=1000)
x = prob.solution[:,0]
x_d = prob.solution[:,1]
plot(x,x_d)
show()

# Part E

mu = 2
omega = 1

def f(r,t):
    x = r[0]
    x_d = r[1]
    fx = x_d
    fx_d =  -omega**2*x + mu*(1-x**2)*x_d
    return array([fx,fx_d],float)


prob = rksolve(f)
prob.initial_conditions=[1,0]
prob.iterate(0,20,N=200)
x = prob.solution[:,0]
x_d = prob.solution[:,1]
plot(x,x_d)


mu = 4
omega = 1

def f(r,t):
    x = r[0]
    x_d = r[1]
    fx = x_d
    fx_d =  -omega**2*x + mu*(1-x**2)*x_d
    return [fx,fx_d]


prob = rksolve(f)
prob.initial_conditions=[1,0]
prob.iterate(0,20,N=10000)
x = prob.solution[:,0]
x_d = prob.solution[:,1]
plot(x,x_d)

show()