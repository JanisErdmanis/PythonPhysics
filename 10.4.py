# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 23:09:33 2013

@author: akels
"""
from __future__ import division, print_function
#from os import sys
#sys.path.append('cpresources')
from pylab import *

from numpy.random import random

N = 100
tau = 3.053*60
mu = log(2)/tau

z = random(N)

t_dec = -1/mu*log(1-z)
t_dec = sort(t_dec)
decayed = arange(1,N+1)

surrived = -decayed + N

plot(t_dec,surrived)