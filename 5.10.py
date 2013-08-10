# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 21:25:08 2013

@author: akels
"""

from __future__ import division, print_function

from os import sys
from numpy import linspace
from pylab import *
sys.path.append('cpresources')
from gaussxw import gaussxw

N = 100
m = 1
V = lambda x: x**4

x,w = gaussxw(N)


def T(a_):
	
	a = 0
	b = a_
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	E = V(a_)
	
	y = 1/sqrt(E-V(xp))
	s = sum(y*wp)

	return s*sqrt(8*m)
	
a = linspace(0,2,100)
periods = [T(ai) for ai in a]

plot(a,periods)
xlabel('initial position')
ylabel('period')