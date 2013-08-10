# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 11:49:08 2013

@author: akels
"""

from __future__ import division, print_function
from math import tanh
from pylab import *

f = lambda x: 1 + 1/2*tanh(2*x)

h = 0.5

x = linspace(-2,2)
f_diff = (f(x + h/2) - f(x - h/2))/h
f_diff_a = -tanh(2*x)**2 + 1

plot(x,f_diff,'--')
plot(x,f_diff_a,'-')