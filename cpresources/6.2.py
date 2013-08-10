# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 18:21:51 2013

@author: akels
"""
from numpy import array,empty

A = array([[ 2,  1,  4,  1 ],
           [ 3,  4, -1, -1 ],
           [ 1, -4,  1,  5 ],
           [ 2, -2,  1,  3 ]], float)
v = array([ -4, 3, 9, 7 ],float)
N = len(v)

# Gaussian elimination
for m in range(N):
	
    # Check if A[m,m] is the largest value from elements bellow and perform swapping
	
    for i in range(m+1,N):
        if A[m,m] < A[i,m]:
            temp = copy(A[m,:])
            A[m,:] = A[i,:]										
            A[i,:] = temp
	
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
