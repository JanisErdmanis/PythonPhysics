# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 00:02:39 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *


def r(r1,r2):
	
	delta = r1 - r2
	length = sqrt(delta[0]**2 + delta[1]**2)
	
	return delta/length**3
	
G = 1
m1 = 150
m2 = 200
m3 = 250

def f(r_,t):
	r1,r2,r3,v1,v2,v3 = r_
	
	Dr1 = v1
	Dr2 = v2
	Dr3 = v3
	
	Dv1 = m2*r(r2,r1) + m3*r(r3,r1)
	Dv2 = m1*r(r1,r2) + m3*r(r3,r2)
	Dv3 = m1*r(r1,r3) + m2*r(r2,r3)
	
	return array([Dr1,Dr2,Dr3,Dv1,Dv2,Dv3],float)
	


class rksolve:
	
	def __init__(self,f):
		
		self.f = f #self.array_decorator(f)
		
		self.initial_conditions = None
		self.solution = None
		
	def iterate(self,a,b,N=1000):
		
		#f = self.f
		r0 = array(self.initial_conditions,float96)
		
		h = (b-a)/N
		
		tpoints = arange(a,b,h)
		solution = empty(tpoints.shape + r0.shape,float)
		
		#r_points[0] = r0
		r = r0
		for i,t in enumerate(tpoints):
		    solution[i]=r
		    r += self.estimate_delta(r,t,h)
		
		self.h = h
		self.solution = solution
		self.t = tpoints
		
	def estimate_delta(self,r,t,h):
		
		f = self.f
		k1 = h*f(r,t)
		k2 = h*f(r+0.5*k1,t+0.5*h)
		k3 = h*f(r+0.5*k2,t+0.5*h)
		k4 = h*f(r+k3,t+h)
		return (k1+2*k2+2*k3+k4)/6

class rksolve_adaptive(rksolve):
	
	def iterate(self,a,b,delta=1):
		
		
		r0 = array(self.initial_conditions,float96)
		
		h = (b-a)/10000
		solution = []
		time = []
		h_list = []
		r = r0
		t = a
		
		solution.append(copy(r))
		time.append(t)
		h_list.append(h)
		
		def distance(r1,r2):
			r1 = r1[:3]
			r2 = r2[:3]
			
			return sqrt(sum((r1-r2)**2))
			
		ro = 1
		while t<b:	
			if ro<2:
				h = h*ro**(1/4)
			else:
				h*=2
				
			if h>1e-3: h = 1e-3
			# estimating ro
			r1 = r + self.estimate_delta(r,t,h)
			r1 += self.estimate_delta(r1,t+h,h)			
			r2 = r + self.estimate_delta(r,t,2*h)
			
			#difference = r1 - r2
			ro = 30*h*delta/distance(r1,r2)  #sqrt(difference[0]**2 + difference[1]**2)
			
			if ro>1:
				t +=2*h
				r = r1
				solution.append(copy(r))
				time.append(t)
				h_list.append(h)
		
		self.h = h_list
		self.solution = array(solution)
		self.t = time

prob = rksolve_adaptive(f)

r1 = [3,1]
r2 = [-1,-2]
r3 = [-1,1]
prob.initial_conditions = [r1,r2,r3,[0,0],[0,0],[0,0]]

prob.iterate(0,2,delta=1e-3)

for i in range(3):
	x = prob.solution[:,i,0]
	y = prob.solution[:,i,1]
	plot(x,y,label=i)
legend()
show()

from visual import sphere, rate

def radius(m):
	
	return m**(1/3)/100

s1 = sphere(radius=radius(150))
s2 = sphere(radius=radius(200))
s3 = sphere(radius=radius(250))

s = [s1,s2,s3]

C = 0.1 
for h,pos in zip(prob.h,prob.solution[:,:3]):
	rate(int(C/h))
		
	for si,posi in zip(s,pos):
		rx,ry = posi
		si.pos = rx,ry,0
	