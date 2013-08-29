# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 11:00:42 2013

@author: akels
"""
from __future__ import division, print_function
from os import sys
sys.path.append('cpresources')
from math import exp

from numpy import array
from numpy.linalg import solve

U = 5
R1 = 1e3
R2 = 4e3
R3 = 3e3
R4 = 2e3
I0 = 3e-9
VT = 100

accuracy = 1e-6
error = 1

I = lambda V1,V2: I0*(exp((V1-V2)/VT)-1)
f1 = lambda V1,V2: -U/R1 + I(V1,V2) + V1*(1/R1 + 1/R2)
f2 = lambda V1,V2: U*(1/R1 + 1/R3) - V1*(1/R1 + 1/R2) - V2*(1/R3 + 1/R4)

V1 = 1
V2 = 5
V1_ = 1.1
V2_ = 4.9
	
for i in range(100):
	
	d1f1 = (f1(V1_,V2) - f1(V1,V2))/(V1_ - V1)
	d2f1 = (f1(V1,V2_) - f1(V1,V2))/(V2_ - V2)
	d1f2 = (f2(V1_,V2) - f2(V1,V2))/(V1_ - V1)
	d2f2 = (f2(V1,V2_) - f2(V1,V2))/(V2_ - V2)
	
	J = [[d1f1, d2f1],
		[d1f2, d2f2]]
		
	b = [f1(V1,V2),f2(V1,V2)]
	
	V1,V2 = V1_,V2_
	V1_,V2_ = array([V1,V2],float) - solve(J,b)
	
	print('V1 = {}\t V2 = {}'.format(V1_,V2_))

#==============================================================================
# 
# for i in range(10):
# 	V1_1,V1_0 = V1_2,V1_1
# 	V2 = (U*(1/R1 + 1/R3) - V1_1*(1/R1 + 1/R2))/(1/R3 + 1/R4)
# 	V1_2 = (U/R1 - I0*(exp((V1_1 - V2)/VT) - 1) )/(1/R1 + 1/R2)
# 	
# 	#error = (V1_1 - V1_2)**2/(2*V1_1 - V1_0 - V1_2)
#==============================================================================