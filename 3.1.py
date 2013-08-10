# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 08:15:04 2013

@author: akels
"""

from pylab import *
from numpy import loadtxt

#gray()

data = loadtxt('./cpresources/sunspots.txt')
month,sunid = data[:,0],data[:,1]

plot(month,sunid)
show()


month,sunid = data[:1000,0],data[:1000,1]

r = 5
s = [ sum(sunid[k-r:k+r]) for k in range(1000)]
y = array(s)/2/r

plot(month,sunid,'g.',label='noisy')
plot(month,y,label='averaged')
legend()
show()
