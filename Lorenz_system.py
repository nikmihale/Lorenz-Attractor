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

ptinput = raw_input("Enter the starting point coordinates separated by commas (try 1, 1, 1) : ")
point = ptinput.split(',')

x, y, z = [float(Fraction(coord.strip())) for coord in point]

sysinput = raw_input("Enter Lorenz system parameters sigma, rho and beta (try 10, 28, 8/3) : ")
system = sysinput.split(',')
sigma, rho, beta = [float(Fraction(param.strip())) for param in system]

numinput = raw_input("Enter step length and total number of points to output (try 100, 2000) : ")
inp = numinput.split(',')
step, num = [abs(int(nmb.strip())) for nmb in inp]

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

for i in range(num):
	xd = float(xdot(sigma, x, y) / step)
	yd = float(ydot(rho, x, y, z) / step) 
	zd = float(zdot(beta, x, y, z) / step)
	ax.scatter(x + xd, y + yd, z + zd, s = 3, c ='b') #s=3 results in rather small points (changeable)
	x, y, z = x + xd, y + yd, z + zd
plt.show()
