import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter=100):
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter

x, y = np.linspace(-2, 1, 1000), np.linspace(-1.5, 1.5, 1000)
img = np.zeros((len(y), len(x)))

for i in range(len(y)):
    for j in range(len(x)):
        img[i, j] = mandelbrot(complex(x[j], y[i]))

plt.imshow(img, cmap="inferno")
plt.colorbar()
plt.show()
