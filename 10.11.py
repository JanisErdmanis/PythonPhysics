# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 21:29:19 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *

N = 50
steps = 100
Tmax = 10
Tmin = 1e-3
tau = 1e4

grid = zeros((N,N),int)
count = 0

from traits.api import HasTraits,CArray, CBool
from visual import rate, sphere, cylinder, color,display
d = display(center=[N//2,N//2])
class dimmer(HasTraits):
	
	
	r_bot = CArray(value=[0,0],dtype=float)
	r_top = CArray(value=[1,0],dtype=float)
	visible = CBool(True)

	def __init__(self):
		self.cylinder = cylinder(radius=0.1)
		self.sphere1 = sphere(radius=0.2)
		self.sphere1.color = color.red
		self.sphere2 = sphere(radius=0.2)
		self.sphere2.color = color.red
	
	#@on_trait_change('pos_top,pos_bot') # Didn't work?
	def _r_bot_changed(self,old,new):	
		self.cylinder.pos = self.r_bot
		self.cylinder.axis = self.r_top - self.r_bot 
		self.sphere2.pos = self.r_bot
		
	def _r_top_changed(self,old,new):
		self.sphere1.pos =  self.r_top
		# Decorator didn't worked
		self.cylinder.axis = self.r_top - self.r_bot 

	def _visible_changed(self,old,new):
		self.sphere1.visible = self.visible
		self.sphere2.visible = self.visible
		self.cylinder.visible = self.visible

class dimer_grid:

	def __init__(self):
		x = range(N)
		y = range(N)
		self.container = empty((N,N,2)).tolist()#[[[None]*2]*N]*N
		
		for i in x:
			for j in y:
				for pos in [0,1]:
					dime = dimmer()
					dime.r_bot = i,j
					
					if pos==0:
						dime.r_top = i+1,j
					else:
						dime.r_top = i, j+1

					dime.visible = False #True						
					self.container[i][j][pos] = dime
					
		
	def index_lattice(f):
		
		def g(self,(i,j),(m,n)):
			
			# correct order
			if i>m or j>n:
				i,j,m,n = m,n,i,j
			
			if i<m:
				pos = 0 # right
			elif j<n:
				pos=1 # bottom
			
			return f(self,i,j,pos)
		return g
	
	@index_lattice
	def add(self,i,j,pos):
		self.container[i][j][pos].visible = True
	
	@index_lattice
	def remove(self,i,j,pos):
		self.container[i][j][pos].visible = False
	
grid_repr = dimer_grid()
grid_repr.remove((1,1),(1,2))
grid_repr.container[10][10][1].visible = False

def setvalue((i,j),(m,n)):
	
	for value in range(1,N*N//2):
		if not value in grid:
			break
	
	grid[i,j] = value
	grid[m,n] = value

T = Tmax
t = 0
while T>Tmin:
	t+=1
	T = Tmax*exp(-t/tau)
	
	if t%10000==0: # for checking progress
		print(T)
	
	# dn = 1 when dimmer is added, 0 do nothing, -1 when dimer is removed
	# First two always happens but when it comes to removing it 
	# it is done with probability exp(-1/T)
	
	i,j = randint(N),randint(N)
	
	# Since it is possible to step out from boundary
	m,n = -1,-1
	while m<0 or m==N or n<0 or n==N:
		k = randint(4)
		m,n = i,j
		if k == 0:
			m+=1
		elif k == 1:
			m-=1
		elif k == 2:
			n+=1
		elif k == 3:
			n-=1
	
	if grid[i,j]==0 and grid[m,n]==0:
		setvalue((i,j),(m,n))
		grid_repr.add((i,j),(m,n))
		count +=1
	
	elif grid[i,j]==grid[m,n]: # because of previous if both aren't 0
		
		if random()<exp(-1/T):
			grid[i,j]=0
			grid[m,n]=0
			count-=1
			grid_repr.remove((i,j),(m,n))
	else:
		pass # Otherwise do nothing