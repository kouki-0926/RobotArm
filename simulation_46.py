import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ, openHand, closeHand, constOpenHand, constCloseHand
from simulation.param import *


t0, tf, dt = np.array([0, 0.7, 0.01])
t = np.arange(t0, tf, dt)
Δ = (tf/4)*0.998

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

x = calc_ξ(xf, x0, tf, Δ, t)
y = calc_ξ(y0, y0, tf, Δ, t)
z = calc_ξ(zf, z0, tf, Δ, t)
α = constCloseHand(tf, Δ, t)
r0_ref_6 = np.array([x, y, z, α])


cir_x0, h, a, b = np.array([93, 60, 31, 160])
cir_t0, cir_tf, cir_dt = np.array([t0, 1.5, dt])
cir_t = np.arange(cir_t0, cir_tf, cir_dt)
cir_Δ = (cir_tf/4)*0.998

x = calc_ξ(x0, cir_x0, tf, Δ, t)
y = calc_ξ(y0, -2*a, tf, Δ, t)
z = calc_ξ(z0, h, tf, Δ, t)
α = constCloseHand(tf, Δ, t)
r0_ref_7 = np.array([x, y, z, α])

θ = calc_ξ(2*np.pi, 0, cir_tf, cir_Δ, cir_t)
x = calc_ξ(cir_x0, cir_x0, cir_tf, cir_Δ, cir_t)
y = -a-a*np.cos(θ)
z = h+b*np.sin(θ)
α = constCloseHand(cir_tf, cir_Δ, cir_t)
r0_ref_8 = np.array([x, y, z, α])

x = calc_ξ(cir_x0, xf, tf, Δ, t)
y = calc_ξ(-2*a, y0, tf, Δ, t)
z = calc_ξ(h, zf, tf, Δ, t)
α = constCloseHand(tf, Δ, t)
r0_ref_9 = np.array([x, y, z, α])

r0_ref_10 = openHand(r0_ref_9, tf, Δ, t)

x = calc_ξ(xf, x0, tf, Δ, t)
y = calc_ξ(y0, y0, tf, Δ, t)
z = calc_ξ(zf, z0, tf, Δ, t)
α = constOpenHand(tf, Δ, t)
r0_ref_11 = np.array([x, y, z, α])

r0_ref = np.block([r0_ref_1,
                   r0_ref_2,
                   r0_ref_3,
                   r0_ref_4,
                   r0_ref_5,
                   r0_ref_6,
                   r0_ref_7,
                   r0_ref_8,
                   r0_ref_9,
                   r0_ref_10,
                   r0_ref_11]).T
simulation_3dof(r0_ref, dt, 46)
