# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:09:42 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

from visual import sphere,rate, display
from numpy.random import randint


L = 101
tau = L*L//6#1e4

pos0 = L//2,L//2 #50,50
#i = 50
#j = 50
grid = zeros((L-1,L-1),bool)

def add(i,j,time=0):
	grid[i,j]=True
	s = sphere(radius=0.5)
	s.pos = i,j #i-50,j-50
	
	color = t/tau#(1-1*exp(-t/tau)) 
	s.color = color,color,color
	print(i,j)

d = display(center=(L//2,L//2))
s = sphere()
s.pos = L,L
d.autoscale = False
s.visible=False
t = 0
while grid[pos0]==False:
	t+=1
	i,j = pos0
	while True:
		a = randint(4)	
		
		# If next position is False!=grid[i,j] then I should add sphere 
		if a==0: #move up
			if i==L-2 or grid[i+1,j]==True: 
				#grid[i,j]==True # I could make a new object 
				add(i,j,time=t)
				break
			else:
				i+=1
		elif a==1:
			if i==0 or grid[i-1,j]==True: 
				add(i,j,time=t)
				break
			else:
				i-=1
		elif a==2:
			if j==L-2 or grid[i,j+1]==True: 
				add(i,j,time=t)
				break
			else:
				j+=1
		elif a==3:
			if j==0 or grid[i,j-1]:
				add(i,j,time=t)
				break
			else:
				j-=1