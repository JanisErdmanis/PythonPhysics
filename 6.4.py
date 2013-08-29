# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 19:18:05 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from pylab import *

from numpy.linalg import solve

A = array([[1/1e3 + 1/2e3 + 1e3j*1e-6,		-1e3j*1e-6,	0],
		[-1000j*1e-6,	1/2e3 + 1/1e3 + 1000j*1e-6*1.5,	-1000j*0.5e-6],
		[0,	-1000j*0.5e-6,	1/1e3 + 2/1e3 + 1000j*0.5e-6]]
,dtype=complex)

v = [3/1e3,3/2e3,3/1e3]

x = solve(A,v)

from cmath import polar

for i,xi in enumerate(x):
	r,theta = polar(xi)
	print("""{}:	V={}		phase={}""".format(i,r,theta*180/pi))
 