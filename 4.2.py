# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 14:13:05 2013

@author: akels
"""

from __future__ import division, print_function
from math import sqrt

print('Please give numbers for: {0}x**2 + {1}x + {2} = 0'.format('a','b','c'))

#s = input()
s = (0.001,1000,0.001)
a,b,c = s#[float(i) for i in s.split(' ')]

x1 = (-b + sqrt(b**2-a*a*c))/2/a
x2 = (-b - sqrt(b**2-a*a*c))/2/a #correct value

x1p = 2*c/(-b - sqrt(b**2 - 4*a*c)) # correct value
x2p = 2*c/(-b + sqrt(b**2 - 4*a*c))

x1c = x1p
x2c = x2

f = lambda x: a*x**2 + b*x +c
print(
"""
The solution to {0}x**2 + {1}x + {2} = 0

With traditional methods:	
	x1 = {3}
	x2 = {4}

With method B:
	x1 = {5}
	x2 = {6}	

Solution C:
	x1 = {7}
	x2 = {8}
""".format(a,b,c,x1,x2,x1p,x2p,x1c,x2c))


