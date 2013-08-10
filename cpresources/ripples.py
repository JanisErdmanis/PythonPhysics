from math import sqrt,sin,pi
from numpy import empty,linspace,sin,mgrid,sqrt
from pylab import imshow,gray,show

wavelength = 5.0
k = 2*pi/wavelength
xi0 = 1.0
separation = 20.0      # Separation of centers in cm
side = 100.0           # Side of the square in cm
points = 500j           # Number of grid points along each side
#spacing = side/points  # Spacing of points in cm


# Calculate the positions of the centers of the circles
x1 = side/2 + separation/2
y1 = side/2
x2 = side/2 - separation/2
y2 = side/2

# Make an array to store the heights
#xi = empty([points,points],float)

# Calculate the values in the array
#==============================================================================
# x = linspace(0,side,points)
# y = linspace(0,side,points)
#==============================================================================
x,y = mgrid[0:side:points,0:side:points]
r1 = sqrt((x-x1)**2+(y-y1)**2)
r2 = sqrt((x-x2)**2+(y-y2)**2)
xi = xi0*sin(k*r1) + xi0*sin(k*r2)

#==============================================================================
# for i in range(points):
#     y = spacing*i
#     for j in range(points):
#         x = spacing*j
#         r1 = sqrt((x-x1)**2+(y-y1)**2)
#         r2 = sqrt((x-x2)**2+(y-y2)**2)
#         xi[i,j] = xi0*sin(k*r1) + xi0*sin(k*r2)
#==============================================================================

# Make the plot
imshow(xi.swapaxes(0,1),origin="lower",extent=[0,side,0,side])
gray()
show()
