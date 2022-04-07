import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_t, calc_r0ref
from simulation.param import hand_open, dt

tf, Δ, t = calc_t(0.3)
tf_s, Δ_s, t_s = calc_t(tf/2)

x0, yR, yL, zT, zB = np.array([175, 0, -160, 150, -100])
yC = (yR+yL)/2
zC = (zT+zB)/2

r0_ref_0 = np.array([[x0, yC, zT, hand_open]]).T
r0_ref_1 = calc_r0ref(r0_ref_0, [x0, yL, zB, hand_open], tf, Δ, t)
r0_ref_2 = calc_r0ref(r0_ref_1, [x0, yC, zT, hand_open], tf, Δ, t)
r0_ref_3 = calc_r0ref(r0_ref_2, [x0, yR, zB, hand_open], tf, Δ, t)
r0_ref_4 = calc_r0ref(r0_ref_3, [x0, yC, zT, hand_open], tf, Δ, t)
r0_ref_5 = calc_r0ref(r0_ref_4, [x0, yL-yC/2, zC, hand_open], tf_s, Δ_s, t_s)
r0_ref_6 = calc_r0ref(r0_ref_5, [x0, yR+yC/2, zC, hand_open], tf_s, Δ_s, t_s)
r0_ref_7 = calc_r0ref(r0_ref_6, [x0, yC, zT, hand_open], tf_s, Δ_s, t_s)

r0_ref = np.block([r0_ref_1,
                   r0_ref_2,
                   r0_ref_3,
                   r0_ref_4,
                   r0_ref_5,
                   r0_ref_6,
                   r0_ref_7]).T
simulation_3dof(r0_ref, dt, 52)
