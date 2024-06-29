import numpy as np
from sympy.abc import x, y
from sympy import lambdify, diff, exp, latex, simplify
from matplotlib import pyplot as plt 

num_mesh_grid = 301
x_arary = np.linspace(-3, 3, num_mesh_grid)
y_array = np.linspace(-3, 3, num_mesh_grid)

xx, yy = np.meshgrid(x_arary, y_array)

f_xy = 3*(1-x)**2*exp(-(x**2)-(y+1)**2)\
       -10*(x/5-x**3-y**5)*exp(-x**2-y**2)\
       -1/3*exp(-(x+1)**2-y**2)
f_xy_fcn = lambdify([x, y], f_xy)
f_xy_zz = f_xy_fcn(xx, yy)

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

ax.plot_wireframe(xx,yy, f_xy_zz,
                  color = [0.5,0.5,0.5],
                  rstride=5, cstride=5,
                  linewidth = 0.25)

ax.set_proj_type('ortho')
ax.set_xlabel('$x$'); ax.set_ylabel('$y$')
ax.set_zlabel('$f(x,y)$')
ax.set_xlim(xx.min(), xx.max()); ax.set_ylim(yy.min(), yy.max())
ax.view_init(azim=-135, elev=30)
plt.tight_layout()
ax.grid(False)
plt.show()