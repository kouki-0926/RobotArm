import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_t, calc_r0ref
from simulation.param import hand_open, dt

tf, Δ, t = calc_t(0.35)
x0, xf, y0, yf, z0, zf = np.array([210, 59, 0, 0, -120, 180])

r0_ref_0 = np.array([[x0, y0, z0, hand_open]]).T
r0_ref_1 = calc_r0ref(r0_ref_0, [xf, y0, z0, hand_open], tf, Δ, t)
r0_ref_2 = calc_r0ref(r0_ref_1, [xf, y0, zf, hand_open], tf, Δ, t)
r0_ref_3 = calc_r0ref(r0_ref_2, [x0, y0, zf, hand_open], tf, Δ, t)
r0_ref_4 = calc_r0ref(r0_ref_3, [x0, y0, z0, hand_open], tf, Δ, t)
r0_ref_5 = calc_r0ref(r0_ref_4, [xf, y0, zf, hand_open], tf, Δ, t)
r0_ref_6 = calc_r0ref(r0_ref_5, [xf, y0, z0, hand_open], tf, Δ, t)
r0_ref_7 = calc_r0ref(r0_ref_6, [x0, y0, zf, hand_open], tf, Δ, t)
r0_ref_8 = calc_r0ref(r0_ref_7, [x0, y0, z0, hand_open], tf, Δ, t)

r0_ref = np.block([r0_ref_1,
                   r0_ref_2,
                   r0_ref_3,
                   r0_ref_4,
                   r0_ref_5,
                   r0_ref_6,
                   r0_ref_7,
                   r0_ref_8]).T
simulation_3dof(r0_ref, dt, 51)
