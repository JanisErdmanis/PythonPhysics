# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:03:25 2013

@author: akels
"""
from __future__ import division, print_function
from pylab import *
from numpy.random import random

N = 500
z1 = random(N)
z2 = random(N)

teta = arccos(1 - 2*z1)
fi = 2*pi*z2

x = sin(teta)*cos(fi)
y = sin(teta)*sin(fi)
z = cos(teta)

pos = zip(x,y,z)

from visual import sphere

for posi in pos:
	sphere(pos=posi,radius=0.02)