# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 20:43:03 2013

@author: akels
"""
from visual import sphere
L = 2
R = 0.3
for i in range(-L,L+1,2):
    for j in range(-L,L+1,2):
        for k in range(-L,L+1,2):
            sphere(pos=[i,j,k],radius=R)
            sphere(pos=[i+1,j+1,k],radius=R)
            sphere(pos=[i,j+1,k+1],radius=R)
            sphere(pos=[i+1,j,k+1],radius=R)
