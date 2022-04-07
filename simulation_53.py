import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_t, calc_r0ref
from simulation.param import hand_open, dt

tf, Δ, t = calc_t(0.3)

xT, xB, yMR, yML, zT, zB = np.array([150, 150, 0, -225, 200, -100])
yT = (yMR+yML)/2
yBR, yBL = np.array([yT+70, yT-70])
zC = (zT+zB)/2+20
xC = (xT+xB)/2

r0_ref_0 = np.array([[xC, yML, zC, hand_open]]).T
r0_ref_1 = calc_r0ref(r0_ref_0, [xC, yMR, zC, hand_open], tf, Δ, t)
r0_ref_2 = calc_r0ref(r0_ref_1, [xB, yBL, zB, hand_open], tf, Δ, t)
r0_ref_3 = calc_r0ref(r0_ref_2, [xT, yT, zT, hand_open], tf, Δ, t)
r0_ref_4 = calc_r0ref(r0_ref_3, [xB, yBR, zB, hand_open], tf, Δ, t)
r0_ref_5 = calc_r0ref(r0_ref_4, [xC, yML, zC, hand_open], tf, Δ, t)

r0_ref = np.block([r0_ref_1,
                   r0_ref_2,
                   r0_ref_3,
                   r0_ref_4,
                   r0_ref_5]).T
simulation_3dof(r0_ref, dt, 53)
