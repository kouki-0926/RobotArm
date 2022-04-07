import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
from simulation.simulation_6dof import simulation_6dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *


t0, tf, Δ = np.array([0, 0.5, 0.124])

x0, xf, y0, yf, z0, zf = np.array([la+lb, la, 0, -150, -lc, lc])
num = 10
t = np.arange(t0, tf+Δ/num, Δ/num)
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)

r0_ref = np.array([x, y, z]).T
simulation_6dof(r0_ref, 4)

# # ===============================  fig  ====================================
# fig = plt.figure(figsize=(10, 5))
# ax = fig.add_subplot(111)

# ax.plot(t, x, label="x")
# ax.plot(t, y, label="y")
# ax.plot(t, z, label="z")

# ax.set_xlabel("時間 $t[s]$")
# ax.set_ylabel("角度 $\\theta[deg]$")

# ax.legend()
# ax.grid()
# plt.show()
# # =============================  end fig  ====================================
