# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 20:39:36 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *
from numpy import load
from traits.api import HasTraits,CArray,Float

data = load('F8.1.npy')


teta1 = data[:,0]
teta2 = data[:,1]


from visual import cylinder,sphere,color, rate
class stick(HasTraits):
	
	
	r_bot = CArray(value=[0,0,0],dtype=float)
	r_top = CArray(value=[0,0,0],dtype=float)

	def __init__(self):
		self.cylinder = cylinder(radius=0.1)
		self.sphere = sphere(radius=0.5)
		self.sphere.color = color.red
	
	#@on_trait_change('pos_top,pos_bot')
	def _r_bot_changed(self,old,new):	
		#print(' r_bot updated')
		self.cylinder.pos = self.r_bot
		self.cylinder.axis = self.r_top - self.r_bot #self.pos_axis

	def _r_top_changed(self,old,new):
		#print('r_top updated')
		#print(self.pos_bot + self.pos_axis)
		self.sphere.pos =  self.r_top#self.pos_bot + self.pos_axis
		# Decorator didn't worked
		self.cylinder.axis = self.r_top - self.r_bot #self.pos_axis
	
from cmath import exp
class system(HasTraits):
	
	teta1 = Float()
	teta2 = Float()
	
	l = 10
	
	def __init__(self):
		
		self.top = stick()
		#self.top.r_top = [5,4,2]
		
		self.bottom = stick()
		
		# How to make it to update automatically
		self.bottom.r_bot = self.top.r_top 

	def _teta1_changed(self,old,new):
		r1 = self.l*exp(self.teta1*1j)
		r2 = r1 + self.l*exp(self.teta2*1j)
		
		self.top.r_top = r1.imag,-r1.real,0
		self.bottom.r_bot = self.top.r_top
		self.bottom.r_top = r2.imag,-r2.real,0
	
	def _teta2_changed(self,old,new): 
		self._teta1_changed(old,new)
#==============================================================================
# test2 = stick()
# test2.pos_axis = [0,4,0]	
# test2.pos_bot = [0,5,1]
#==============================================================================

s = system()

s.teta2 = 0.5
s.teta1 = 1

tpoints = linspace(0,100,len(data))
for t,teta1i,teta2i in zip(tpoints,teta1,teta2)[::int(1e3/30)]:
	rate(30)
	print('t={}'.format(t))
	s.teta2 = teta2i
	s.teta1 = teta1i
