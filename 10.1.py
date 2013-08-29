# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 21:04:05 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *
from random import randint

a = randint(1,6)
b = randint(1,6)
print('{}\t{}'.format(a,b))

count = 0
for i in range(1000000):
	a = randint(1,6)
	b = randint(1,6)
	if a==6 and b==6:
		count+=1

probability = count/1e6
print('The observed propability for rolling dice is {}'.format(probability))