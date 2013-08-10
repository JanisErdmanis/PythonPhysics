from visual import sphere,rate
from math import cos,sin,pi
from numpy import arange

s = sphere(pos=[1,0,0],radius=0.1)
for theta in arange(0,10*pi,0.1):
    rate(30)
    x = cos(theta)
    y = sin(theta)
    s.pos = [x,y,0]
