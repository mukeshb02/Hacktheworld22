import numpy as np
from matplotlib import pyplot as plt

theta = np.linspace(0, 2 * np.pi, 100)

x = 16 * ( np.sin(theta) ** 3 )
y = 13 * np.cos(theta) - 5* np.cos(2*theta) - 2 * np.cos(3*theta) - np.cos(4*theta)

plt.plot(x, y, color='red')
plt.show()