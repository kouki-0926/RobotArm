import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ, closeHand, openHand, constCloseHand, calc_r0ref
from simulation.param import *

t0, tf, dt = np.array([0, 0.7, 0.01])
t = np.arange(t0, tf, dt)
Δ = (tf/4)*0.998
cir_t0, cir_tf, cir_dt = np.array([t0, 1.5, dt])
cir_t = np.arange(cir_t0, cir_tf, cir_dt)
cir_Δ = (cir_tf/4)*0.998

x0, xf, y0, yf, z0, zf = np.array([50, la, 0, -181.5, 200, -120])
cir_x0, h, a, b = np.array([93, 60, 31, 160])


r0_ref_0 = np.array([[x0, y0, z0, hand_open]]).T
r0_ref_1 = calc_r0ref(r0_ref_0, [xf, y0, zf, hand_open], tf, Δ, t)
r0_ref_2 = closeHand(r0_ref_1, tf, Δ, t)
r0_ref_3 = calc_r0ref(r0_ref_2, [x0, y0, z0, hand_close], tf, Δ, t)
r0_ref_4 = calc_r0ref(r0_ref_3, [x0, yf, z0, hand_close], tf, Δ, t)
r0_ref_5 = calc_r0ref(r0_ref_4, [xf, y0, zf, hand_close], tf, Δ, t)
r0_ref_6 = calc_r0ref(r0_ref_5, [x0, y0, z0, hand_close], tf, Δ, t)
r0_ref_7 = calc_r0ref(r0_ref_6, [cir_x0, -2*a, h, hand_close], tf, Δ, t)

θ = calc_ξ(2*np.pi, 0, cir_tf, cir_Δ, cir_t)
x = calc_ξ(cir_x0, cir_x0, cir_tf, cir_Δ, cir_t)
y = -a-a*np.cos(θ)
z = h+b*np.sin(θ)
α = constCloseHand(cir_tf, cir_Δ, cir_t)
r0_ref_8 = np.array([x, y, z, α])

r0_ref_9 = calc_r0ref(r0_ref_8, [xf, y0, zf, hand_close], tf, Δ, t)
r0_ref_10 = openHand(r0_ref_9, tf, Δ, t)
r0_ref_11 = calc_r0ref(r0_ref_10, [x0, y0, z0, hand_open], tf, Δ, t)

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
simulation_3dof(r0_ref, dt, "46_1")
