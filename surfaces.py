import numpy as np
import matplotlib.pyplot as plt

x, y = np.meshgrid(np.arange(-500, 501, 5), np.arange(-500, 501, 5))

z = -x * np.sin(np.sqrt(np.abs(x))) - y * np.sin(np.sqrt(np.abs(y)))
x = x / 250
y = y / 250

r = 100 * (y - x**2)**2 + (1 - x)**2
r1 = (y - x**2)**2 + (1 - x)**2
rd = 1 + r1

x1 = 25 * x
x2 = 25 * y
xs = np.arange(-10, 10.1, 0.1)
ys = np.arange(-10, 10.1, 0.1)
a = 500
b = 0.1
c = 0.5 * np.pi

F10 = -a * np.exp(-b * np.sqrt((x1**2 + x2**2) / 2)) - np.exp((np.cos(c * x1) + np.cos(c * x2)) / 2) + np.exp(1)

nx = len(xs)
ny = len(ys)
zsh = np.zeros((nx, ny))

for i in range(nx):
    for j in range(ny):
        zsh[i, j] = 0.5 - ((np.sin(np.sqrt(xs[i]**2 + ys[j]**2)))**2 - 0.5) / (1 + 0.1 * (xs[i]**2 + ys[j]**2))**2

Fobj = F10 * zsh

w = r * z
w1 = r + z
w2 = z - r1
w3 = r - z
w4ant = np.sqrt(r**2 + z**2)
w4 = np.sqrt(r**2 + z**2) + Fobj
w5 = w - 0.5 * w1
w6 = w + w2
w7 = w1 + w4
w8 = w1 - w4
w9 = w2 - w4
w10 = w2 + w4
w11 = w3 - w4
w12 = r + w4 * np.cos(y)
w13 = np.sqrt(w1) + np.sqrt(w3) - w4ant * np.cos(x)
w14 = z * np.exp(np.sin(r1))
w15 = z * np.exp(np.cos(r1))
w16 = w14 + w4
w17 = -w14 + w4
w18 = -w15 + w4
w19 = np.exp(-r1) * z
w20 = x * z
w21 = (x + y) * z
w22 = (x - y) * z
w23 = z / rd
w24 = (x - y) * w23
w25 = (x + y) * w23
w26 = -w4 / rd
w27 = w4 + w23
w28 = w4 - w23
w29 = w14 + w23
w30 = w4 + w14 + w23
w31 = w21 + w22
w32 = w21 + w23
w33 = w22 + w25
w34 = w22 + w26
w35 = w23 + w27

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x, y, w35, cmap='viridis')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('w35')

plt.show()
