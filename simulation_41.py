import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *

# tf_min=0.45
t0, tf, dt = np.array([0, 0.50, 0.01])
t = np.arange(t0, tf, dt)
Δ = (tf/4)*0.998

# z_min=-120
x0, xf, y0, yf, z0, zf = np.array([50, la, 0, 0, 250, -120])
α0, αf, αf_2 = np.array([0, 0, 65])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
α = calc_ξ(α0, αf, tf, Δ, t)
r0_ref_1 = np.array([x, y, z, α])

x = calc_ξ(xf, xf, tf, Δ, t)
y = calc_ξ(yf, yf, tf, Δ, t)
z = calc_ξ(zf, zf, tf, Δ, t)
α = calc_ξ(αf, αf_2, tf, Δ, t)
r0_ref_2 = np.array([x, y, z, α])

x = calc_ξ(xf, x0, tf, Δ, t)
y = calc_ξ(yf, y0, tf, Δ, t)
z = calc_ξ(zf, z0, tf, Δ, t)
α = calc_ξ(αf_2, αf_2, tf, Δ, t)
r0_ref_3 = np.array([x, y, z, α])

r0_ref = np.block([r0_ref_1, r0_ref_2, r0_ref_3]).T
simulation_3dof(r0_ref, dt, 41)
