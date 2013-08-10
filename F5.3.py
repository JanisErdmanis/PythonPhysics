# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:02:33 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from gaussxw import gaussxw
from pylab import *

q = 1
epsilon = 1e-7
#L = 1
#==============================================================================
# 
# x,y = mgrid[-0.5:0.5:100j,0.5:0.5:100j]
# r1 = sqrt((x-0.05)**2 + y**2)
# r2 = sqrt((x+0.05)**2 + y**2)
#==============================================================================

h = 0.01
fi = empty((100,100))
for i,x in enumerate(arange(-0.5,0.5,h)):
	for j,y in enumerate( arange(-0.5,0.5,h)):
		r1 = 	sqrt((x-0.05)**2 + y**2)
		r2 = sqrt((x+0.05)**2 + y**2)
		fi[i,j] =  q/4/pi/epsilon*(1/r1 - 1/r2)

style_charges = {
	'potential':{'vmax':1e7,'vmin':-1e7},
	'magnitude':{'vmax':1e8}
	#'direction':{}
} 

def results(fi,style=style_charges):
	
	imshow(fi,origin='lower',**style['potential'])
	show()
	
	# Partial derivatives
	h = 0.01
	
	fi_x = empty((100,100))
	fi_y = empty((100,100))
	#magnitude = empty((100,100))
	for i in range(1,100-1):
		for j in range(1,100-1):
			fi_x[i,j] = (fi[i+1,j] - fi[i-1,j])/h/2
			fi_y[i,j] = (fi[i,j+1] - fi[i,j-1])/h/2
	
	magnitude = sqrt(fi_x**2 + fi_y**2)
	direction = angle(fi_x + 1j*fi_y)
	
	imshow(magnitude,**style['magnitude'])
	show()
	
	hsv()
	imshow(direction)
	show()

#results(fi)

# Part C

q0 = 10
L = 0.1
ro = lambda x,y: q0*sin(2*pi*x/L)* sin(2*pi*y/L)

# x_ and y_ specifies place where the potential is calculated

#f = lambda x,y,x_,y_: ro(x,y)/sqrt((x_-x)**2 + (y_ - y)**2)

N = 10
x,w = gaussxw(N)
a = -L/2
b = L/2
xp = 0.5*(b-a)*x + 0.5*(b+a)
yp = xp	
wp = 0.5*(b-a)*w
	
def fi_f(x_,y_):
	s=0
	
# Should try to use cpython to improve speed	
	for i,xi in enumerate(xp):
		for j,yj in enumerate(yp):		
			r = sqrt((x_-xi)**2 + (y_ - yj)**2)

			if r>1e-6: #Othervise potential will blow up
				f = ro(xi,yj)/r
			else:
				f = 0
				
			s+=wp[i]*wp[j]*f
		
	return s/4/pi/epsilon
	
fi_continius = empty((100,100))

for i,xi in enumerate(arange(-0.5,0.5,h)):
	for j,yi in enumerate( arange(-0.5,0.5,h)):
		fi_continius[i,j] = fi_f(xi,yi)
 
results(fi_continius)
