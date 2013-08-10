# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 16:40:49 2013

@author: akels
"""

from __future__ import division, print_function

from numpy import linspace, sqrt
from math import pi
N = 100000000
h = 2/N
x = linspace(-1,1,N)
y = sqrt(1 - x**2)

I = h*sum(y)*2
delta = I - pi
print('The value of integral is I = {}'.format(I))
print('delta = {}'.format(delta))