# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:08:55 2013

@author: akels
"""
from __future__ import division, print_function

from numpy import array,empty

A = array([[ 4,-1,-1,-1 ],
           [ -1,0,3,0 ],
           [ -1,3,0,-1 ],
           [ -1,-1,0,4]], float)
v = array([ 5, 5, 0, 0 ],float)
N = len(v)

# Gaussian elimination
for m in range(N):

    # Divide by the diagonal element
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div

    # Now subtract from the lower rows
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

# Backsubstitution
x = empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)
