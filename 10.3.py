# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:02:27 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from visual import sphere,rate, display
from random import randint


L = 101

i = 50
j = 50

d = display()
s = sphere()
s.pos = i,j,0
d.autoscale = False
for t in arange(1e6):
	rate(30)
	s.pos = i-50,j-50,0
	a = randint(1,4)	
	if a==1: #move up
		if i==L: continue
		i+=1
	elif a==2:
		if i==0: continue
		i-=1
	elif a==3:
		if j==L: continue
		j+=1
	elif a==4:
		if j==0: continue
		j-=1