import numpy as np
from simulation.simulation_6dof import simulation_6dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *


t0, tf, Δ = np.array([0, 0.5, 0.124])
num = 15

x0, xf, y0, yf, z0, zf = np.array([la, la+lb, 0, 0, -(ld+140), 120])
t = np.arange(t0, tf+Δ/num, Δ/num)
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_1 = np.array([x, y, z])


x0, xf, y0, yf, z0, zf = np.array([la+lb, la, 0, 0, 120, -(ld+140)])
t = np.arange(t0, tf+Δ/num, Δ/num)
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_2 = np.array([x, y, z])

r0_ref = np.block([r0_ref_1, r0_ref_2]).T
simulation_6dof(r0_ref, 6)
