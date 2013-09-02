# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:14:55 2013

@author: akels
"""
from __future__ import division, print_function
from numpy import array,arange,copy
from pylab import *

# Didn't work?

def f_(r,u,E):
	r"""
	The function is
	
	.. math::	
		\frac{d^2 \psi}{du^2} = \frac{2m}{h^2(1-u)^4}[E - V(\frac{u}{1-u})] + \frac{2}{1-u}\frac{d\psi}{du}
	
	"""
	ksi, teta = r
	Dksi = teta
	Dteta = 2*m/hbar**2/(1-u)**4*(E - V(u/(1-u))*ksi + 2/(1-u)*teta )	
	return array([Dksi,Dteta],float)

# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
a = 1e-11
V0 = 50*e
L = 5*a     # Bohr radius
N = 1000
h = 2*L/N

# Potential function
def V(x):
    return V0*x**4/a**4

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy
#solution = []
def solve(E):
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)
#    solution = []
    for x in arange(-L,L,h):
        #solution.append(r)
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0] #array(solution) #r[0]

# Main program to find the energy using the secant method
def energy(E=0):
	
	E*=e
	E1 = E#0.0
	E2 = E + e
	psi2 = solve(E1)
	
	target = e/1000
	while abs(E1-E2)>target:
	    psi1,psi2 = psi2,solve(E2)
	    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)
	
	print("E =",E2/e,"eV")
	return E2/e
	
Energies = [205.3,735.7,1443.6]


def solution(E):
    E *=e
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)
    result = []
    for x in arange(-L,L,h):
        result.append(copy(r))
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return array(result,float)[:,0] #array(solution) #r[0]

precise = lambda E: solution(energy(E))

from scipy.integrate import simps

for Ei in [100,700,1400]:
	y = precise(Ei)
	Iy = simps(y**2)
	plot(y/sqrt(Iy),label=Ei)

legend()
show()