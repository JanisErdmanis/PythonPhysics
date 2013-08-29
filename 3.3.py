# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:31:04 2013

@author: akels
"""
from __future__ import division, print_function

from visual import sphere,color
L = 5
R = 0.3
for i in range(-L,L+1,2):
    for j in range(-L,L+1,2):
        for k in range(-L,L+1,2):
            sphere(pos=[i,j,k],radius=R,color=color.red)

for i in range(-L+1,L,2):
    for j in range(-L+1,L,2):
        for k in range(-L+1,L,2):
            sphere(pos=[i,j,k],radius=R*2,color=color.cyan)