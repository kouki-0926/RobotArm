import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *

t0, tf, Δ = np.array([0, 0.5, (0.5/4)*0.99])
num = 54
t, dt = np.linspace(t0, tf, num, retstep=True)

xmin, xmax = [la+lb-90, la+lb-70]
ymin, ymax = [-100, 0]
zmin, zmax = [-70, 168]

x0, xf, y0, yf, z0, zf = np.array([xmin, xmax, ymin, ymax, zmin, zmax])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_1 = np.array([x, y, z])


x0, xf, y0, yf, z0, zf = np.array([xmax, xmin, ymax, ymin, zmax, zmin])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_2 = np.array([x, y, z])

r0_ref = np.block([r0_ref_1, r0_ref_2]).T
simulation_3dof(r0_ref, dt, 11)
