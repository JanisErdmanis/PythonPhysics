# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 21:21:27 2013

@author: akels
"""
from __future__ import division, print_function
from visual import sphere, display, color, rate
from cmath import exp
from math import pi
#from numpy import empty


sphere(pos=(0,0,0),radius=40,color=color.yellow)

c1 = 2e-3
c2 = 0.5

class planet:	
	
	def __init__(self,r_radius,r_orbit,period):
	#self = sphere()
		
		self.sphere = sphere()
		print("Object {} created".format([r_radius,r_orbit,period]))
		
		self.T = period
		self.r_orbit = r_orbit #108.2e6/100
		self.sphere.radius = r_radius #6052
		
		self.move(0)		
				
	def move(self,t):
		
		omega = 2*pi/self.T
		teta = omega*t
		
		pos = self.r_orbit*exp(1j*teta)
		self.sphere.pos = [pos.real,pos.imag,0]

## Not a good example because array has to be with dtype planet		
#==============================================================================
# class configuration(array):
# 	"""
# Shuld bind all objects together with time. Subclass of array
# 	"""
# 	def move(self,t):
# 		"""
# 	Moves all planets to new positions
# 		"""
# 		for i in self:
#			self.move(t)
#==============================================================================
			

table = [
	[2440,	57.9,		88,	color.red],
	[6052,	108.2,	224.7, color.magenta],
	[6371,	149.6	,	365.3, color.blue],
	[3386,	227.9,	687.0, color.orange],
	[69173,	778.5,	4331.6,color.magenta],
	[57316,	1433.4,	10759.2,color.green]]

planets = []
for r_radius,r_orbit,period,color in table:
	s = planet(r_radius*c1,r_orbit,period/c2)
	s.sphere.color = color
	planets.append(s)
	
d = display()
d.autoscale = False

t = 0
while True:
	rate(30)
	for i in planets:
		i.move(t*c2)
	t+=1

