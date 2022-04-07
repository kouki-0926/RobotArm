# eps=1e-3 の時, 逆運動学が収束
from matplotlib import gridspec
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *


t0, tf, Δ = np.array([0, 0.5, 0.5/4*0.999])
num = 42
t, dt = np.linspace(t0, tf, num, retstep=True)
stop_step = 25

α = 0.00
β = la+lb-α
l = 0.2910*β
x0, xf, y0, yf, z0, zf = np.array([β-l, β-l,
                                   0, 0,
                                   np.sqrt(2*l*β-l**2), 0])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_1 = np.array([x, y, z])
r0_ref_1_2 = np.array([r0_ref_1[:, -1] for i in range(stop_step)]).T


x0, xf, y0, yf, z0, zf = np.array([β-l, β-l,
                                   0, -np.sqrt(2*l*β-l**2),
                                   0, 0])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_2 = np.array([x, y, z])
r0_ref_2_2 = np.array([r0_ref_2[:, -1] for i in range(stop_step)]).T


x0, xf, y0, yf, z0, zf = np.array([β-l, β-l,
                                   -np.sqrt(2*l*β-l**2), 0,
                                   0, np.sqrt(2*l*β-l**2)])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_3 = np.array([x, y, z])
r0_ref_3_2 = np.array([r0_ref_3[:, -1] for i in range(stop_step)]).T


r0_ref = np.block([r0_ref_2, r0_ref_2_2,
                   r0_ref_3, r0_ref_3_2,
                   r0_ref_1, r0_ref_1_2]).T
simulation_3dof(r0_ref, dt, 8)

# # ===============================  fig  ====================================
# size = 0.85
# fig = plt.figure(figsize=(16*size, 9*size))
# spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[1.2, 2])
# # ===============================  fig1  ===================================
# ax = fig.add_subplot(spec[1], projection='3d')
# ax.plot(r0_ref[:, 0], r0_ref[:, 1], r0_ref[:, 2], "-", color="green")
# ax.set_xlim(-250, 250)
# ax.set_ylim(-250, 250)
# ax.set_zlim(-170, 170)
# ax.set_xlabel("$x_0$")
# ax.set_ylabel("$y_0$")
# ax.set_zlabel("$z_0$")
# # ax.legend()
# ax.grid()
# # ===============================  fig2  ===================================
# ax2 = fig.add_subplot(spec[0])
# t_ax2 = np.arange(0, r0_ref.shape[0]*dt, dt)
# ax2.plot(t_ax2, r0_ref[:, 0], label="x")
# ax2.plot(t_ax2, r0_ref[:, 1], label="y")
# ax2.plot(t_ax2, r0_ref[:, 2], label="z")
# ax2.set_xlabel("時間 $t[s]$")
# ax2.set_ylabel("座標 $x, y, z [m]$")
# ax2.legend()
# ax2.grid()

# fig.tight_layout()
# plt.show()
# # =============================  end fig  ====================================

# print(np.min(r0_ref[:, 0]))
# print(np.min(r0_ref[:, 1]))
# print(np.max(r0_ref[:, 2]))
