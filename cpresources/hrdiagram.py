from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt

data = loadtxt("stars.txt",float)
x = data[:,0]
y = data[:,1]

plot(x,y,'k.')
xlabel("Temperature")
ylabel("Magnitude")
xlim(13000,0)
ylim(20,-5)
show()
