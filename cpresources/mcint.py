from math import sin
from random import random

def f(x):
    return (sin(1/(x*(2-x))))**2

N = 10000
count = 0
for i in range(N):
    x = 2*random()
    y = random()
    if y<f(x):
        count += 1
I = 2*count/N
print(I)
