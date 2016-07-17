import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from fractions import Fraction

def xdot(sigma, x, y):
	return sigma * ( y - x )

def ydot(rho, x, y, z):
	return x * (rho - z) - y

def zdot(beta, x, y, z):
	return x * y - beta * z

#x, y, z = 1, 1, 1
#sigma, rho, beta = 10, 28, 8/3
ptinput = raw_input("Enter the starting point coordinates separated by commas (try 1, 1, 1) : ")
point = ptinput.split(',')

x, y, z = [float(Fraction(coord.strip())) for coord in point]

sysinput = raw_input("Enter Lorenz system parameters sigma, rho and beta (try 10, 28, 8/3) : ")
system = sysinput.split(',')
sigma, rho, beta = [float(Fraction(param.strip())) for param in system]

step = 100

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

for i in range(200):
	xd = float(xdot(sigma, x, y) / step)
	yd = float(ydot(rho, x, y, z) / step) 
	zd = float(zdot(beta, x, y, z) / step)
	ax.scatter(x + xd, y + yd, z + zd, s = 5, c ='b')
	x, y, z = x + xd, y + yd, z + zd
plt.show()