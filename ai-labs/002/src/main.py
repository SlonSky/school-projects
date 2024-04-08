from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

A = 2
B = 5
C = 1
D = 3
E = 1
F = 2
G = -1
H = 3
K = 4
M = 7
N = 2
P = -1
Q = 4
R = -6
S = 5
V = -1
W = -1
Z = 2

def d12(x, y):
    return A * y + B * x + C

def d13(x, y):
    return D * y + E * x + F

def d23(x, y):
    return G * y + H * x + K

def d1(x, y):
    return M * y + N * x + P

def d2(x, y):
    return Q * y + R * x + S

def d3(x, y):
    return V * y + W * x + Z

X = np.arange(-100, 100, 1)
Y = np.arange(-100, 100, 1)

class1 = [];
class2 = [];
class3 = [];

def color(x, y):
    if d12(x, y) > 0 and d13(x, y) > 0:
        class1.append([x, y])
    if d12(x, y) < 0 and d23(x, y) > 0:
        class2.append([x, y])
    if d13(x, y) < 0 and d23(x, y) < 0:
        class3.append([x, y])

for x in X:
    for y in Y:
        color(x, y)

class1 = np.array(class1)
class2 = np.array(class2)
class3 = np.array(class3)

plt.plot(class1[:, 0], class1[:, 1], '.r')
plt.plot(class2[:, 0], class2[:, 1], '.g')
plt.plot(class3[:, 0], class3[:, 1], '.b')

plt.show()
