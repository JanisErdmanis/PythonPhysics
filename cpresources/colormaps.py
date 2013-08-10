# Color maps module

from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import RdBu
from matplotlib.pyplot import set_cmap

cdict = {'red':   [(0.0,1.0,1.0),(0.5,0.0,0.0),(1.0,0.0,0.0)],
         'green': [(0.0,0.0,0.0),(1.0,0.0,0.0)],
         'blue':  [(0.0,0.0,0.0),(0.5,0.0,0.0),(1.0,1.0,1.0)]}
cp_redblue = LinearSegmentedColormap("redblue",cdict)

cp_redwhiteblue = RdBu

cdict = {'red':   [(0.0,1.0,1.0),(1.0,0.0,0.0)],
         'green': [(0.0,1.0,1.0),(1.0,0.0,0.0)],
         'blue':  [(0.0,1.0,1.0),(1.0,0.0,0.0)]}
cp_inversegray = LinearSegmentedColormap("inversegray",cdict)

def redblue():
    set_cmap(cp_redblue)

def redwhiteblue():
    set_cmap(cp_redwhiteblue)

def inversegray():
    set_cmap(cp_inversegray)
