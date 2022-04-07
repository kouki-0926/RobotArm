import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ, openHand, closeHand, constOpenHand, constCloseHand
from simulation.param import *


# tf_min=0.45
t0, tf, dt = np.array([0, 0.8, 0.01])
t = np.arange(t0, tf, dt)
Δ = (tf/4)*0.998

# z_min=-120
# z_max=250
x0, xf, y0, yf, z0, zf = np.array([50, la, 0, -181.5, 200, -120])
α0, αf = np.array([0, 65])

x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, y0, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
α = constOpenHand(tf, Δ, t)
r0_ref_1 = np.array([x, y, z, α])

r0_ref_2 = closeHand(r0_ref_1, tf, Δ, t)

x = calc_ξ(xf, x0, tf, Δ, t)
y = calc_ξ(y0, y0, tf, Δ, t)
z = calc_ξ(zf, z0, tf, Δ, t)
α = constCloseHand(tf, Δ, t)
r0_ref_3 = np.array([x, y, z, α])

x = calc_ξ(x0, x0, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, z0, tf, Δ, t)
α = constCloseHand(tf, Δ, t)
r0_ref_4 = np.array([x, y, z, α])

x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(yf, y0, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
α = constCloseHand(tf, Δ, t)
r0_ref_5 = np.array([x, y, z, α])

r0_ref_6 = openHand(r0_ref_5, tf, Δ, t)

x = calc_ξ(xf, x0, tf, Δ, t)
y = calc_ξ(y0, y0, tf, Δ, t)
z = calc_ξ(zf, z0, tf, Δ, t)
α = constOpenHand(tf, Δ, t)
r0_ref_7 = np.array([x, y, z, α])

r0_ref = np.block([r0_ref_1,
                   r0_ref_2,
                   r0_ref_3,
                   r0_ref_4,
                   r0_ref_5,
                   r0_ref_6,
                   r0_ref_7]).T
simulation_3dof(r0_ref, dt, 42)
