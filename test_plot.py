import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

from scipy.stats import expon, multivariate_normal

x = np.linspace(-1, 1, 101)
y = np.linspace(-1, 1, 101)
_x, _y = np.meshgrid(x, y, indexing='ij')
z = multivariate_normal([0.5, -0.2], [[2.0, 0.3], [0.3, 0.5]]).pdf(np.c_[_x.ravel(), _y.ravel()])
xz = z.reshape(x.size, y.size).max(axis=1)
yz = z.reshape(x.size, y.size).max(axis=0)

gs = GridSpec(2, 2)
fig = plt.figure()
ax = fig.add_subplot(gs[0, 0], projection='3d')
ax.plot_surface(_x, _y, z.reshape(x.size, y.size), cmap='jet')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax = fig.add_subplot(gs[0, 1], aspect='equal')
ax.pcolormesh(_x, _y, z.reshape(x.size, y.size), cmap='jet')
ax.set_xlabel('x')
ax.set_ylabel('y')

ax = fig.add_subplot(gs[1, 0])
ax.plot(x, xz)
ax.axis([-1., 1., z.min(), z.max() + 0.01])
ax.set_xlabel('x')
ax.set_ylabel('z')

ax = fig.add_subplot(gs[1, 1])
ax.plot(y, yz)
ax.axis([-1., 1., z.min(), z.max() + 0.01])
ax.set_xlabel('y')
ax.set_ylabel('z')

plt.tight_layout()
plt.show()
# plt.savefig('img1.png')
