from pylab import imshow,show, gray
from numpy import loadtxt

data = loadtxt("circular.txt",float)
imshow(data,origin='lower',extent=[0,10,2,7])
gray()
show()
