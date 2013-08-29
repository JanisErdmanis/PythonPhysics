# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:32:33 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

from visual import sphere, display
from numpy.random import randint


L = 201
tau = L*L//6#1e4

#i = 50
#j = 50

def add(i,j,time=tau):
	grid[i,j]=True
	s = sphere(radius=0.5)
	s.pos = i,j #i-50,j-50
	
	color = 1 #time/tau#(1-1*exp(-t/tau)) 
	s.color = color,color,color
	#print(i,j)

def circle(r=0):
	"""
	Generates i,j randomly on the circle with radius r+1
	"""
	teta = 2*pi*random()
	x = (r+1)*cos(teta) + L//2
	y = (r+1)*sin(teta) + L//2
	
	i = int(x) + 1
	j = int(y) + 1
	print(r)
	return i,j

def radius(i,j):
	
	dx = i - L//2
	dy = j - L//2
	
	distance = sqrt(dx**2 + dy**2)
	#print(dx,dy)
	return distance
	

# Configuring view
d = display(center=(L//2,L//2))
s = sphere()
s.pos = L,L
d.autoscale = False
s.visible=False

grid = zeros((L,L),bool)
center = L//2,L//2 #50,50
add(*center)
t = 0
r = 1
while r*2<L//2:
	t+=1
	
	i,j = circle(r)
	ri = 0
	while ri<=2*r:
		a = randint(4)	
		# If next position is False!=grid[i,j] then I should add sphere 
		newi,newj = i,j
		if a==0: #move up
			newi+=1
		elif a==1:
			newi-=1
		elif a==2:
			newj+=1
		elif a==3:
			newj-=1
			
		if grid[newi,newj]==True:
			add(i,j,time=t)
			if r<ri: r = int(ri)
			break
		else:
			i,j = newi, newj
		ri = radius(i,j)
		
else:
	print('Sucesfully filled')