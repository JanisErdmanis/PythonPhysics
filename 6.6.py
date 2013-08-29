# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:23:35 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from numpy.linalg import solve
from numpy import  array, empty, zeros

from banded import banded

# Test with 6 elements

N = 6
U = 5

A = array([
	[3, -1, -1, 0, 0, 0],
	[-1, 4, -1, -1, 0, 0],
	[-1,-1, 4, -1, -1, 0],
	[0, -1,-1, 4, -1, -1],
	[0, 0, -1,-1, 4, -1],
	[0, 0, 0, -1, -1, 3]
],float)

v = array([U, U, 0, 0, 0, 0],float)

x = solve(A,v)
print(x)

# Banded example

N = 10000
Ab = empty((5,N),float)
vb = zeros(N,float)

vb[[0,1]] = U

Ab[:,:] = -1
Ab[2,:] = 4
Ab[2,0] = 3
Ab[2,N-1] = 3

x = banded(Ab,vb,2,2)
print(x)