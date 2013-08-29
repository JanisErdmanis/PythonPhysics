# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 12:04:20 2013

@author: akels
"""
from __future__ import division, print_function
from math import sin,pi
from numpy import array,arange
from pylab import plot,xlabel,show

g = 9.81
l =0.1

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -g/l*sin(theta)
    return array([ftheta,fomega],float)

a = 0.0
b = 10.0
N = 3000
h = (b-a)/N

tpoints = arange(a,b,h)
theta = []

r = array([179/180*pi,0],float)
for t in tpoints:
    theta.append(r[0])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plot(tpoints,theta)
#plot(tpoints,ypoints)
xlabel("t")
show()


class pendulum_xyz:
	
	def __init__(self,length):
		
		self.length = length
		
		from visual import sphere, cylinder,box,color

		self.cylinder = cylinder(radius=0.1)
		#self.cylinder.axis = self.x,self.y,self.z
		
		self.sphere = sphere(radius=0.5)
		self.sphere.color = color.red
		#self.sphere.pos = self.x,self.y,self.z
		#self.update_pos()
		
		self.box = box(lenght=2,width=2,height=0.1)
		self.box.pos = 0,0,-0.1/2
		
		#self.pos = pos
		self.setpos([0,length,0]) 
		#d = display()
	
	#@property
	def getpos(self):
		print('Getting position')
		return self._pos
	
	#@pos.setter
	def setpos(self,pos):
		pos[1]=-pos[1]
		print('Position set to {}'.format(pos))
		self._pos = pos
		self.cylinder.axis = pos
		self.sphere.pos = pos
	
	#pos = property(getpos,setpos)

class pendulum_theta(pendulum_xyz):
	
	from cmath import exp
	
	#def __init__(self)
	
	def angle(self,theta):
		
		r = self.length*exp(1j*theta)
		self.setpos([r.imag,r.real,0])

	
p = pendulum_theta(10)

from visual import rate

for t,angle in zip(tpoints,theta)[::10]:
	rate(30)
	#print('t={}\ttheta={}'.format(t,angle))
	p.angle(angle)
