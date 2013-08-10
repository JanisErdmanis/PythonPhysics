# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 11:22:39 2013

@author: akels
"""

from pylab import *

def logmap(r,x=1./2,n=1000):
	"""
	By using equation $x <- rx(1-x)$ n times the value is returned
	"""
	for i in range(n):
		x = r*x*(1-x)
	return x
	
r = arange(1,4,0.01)
x = logmap(r)
#x = [logmap(ri) for ri in r]

plot(r,x,'k.')
xlabel('r')
ylabel('x')