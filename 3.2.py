# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 10:17:58 2013

@author: akels
"""

from numpy import *
from pylab import *

data = loadtxt('cpresources/stm.txt')
gray()
imshow(data)
xlim(150,550)
ylim(100,500)