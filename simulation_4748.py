import sys
import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import circle, ellipse, closeHand, openHand, calc_r0ref, calc_t
from simulation.param import *

# ==================================
try:
    file_num = int(sys.argv[1])
except:
    file_num = 47
# ==================================

tf, Δ, t = calc_t(0.40)
cir_tf, cir_Δ, cir_t = calc_t(1.7)
tf, Δ, t = calc_t(0.70)
cir_tf, cir_Δ, cir_t = calc_t(2.0)


x0, xf, y0, yf, z0, zf = np.array([50, la, 0, -181.5, 200, -120])
if file_num == 47:
    h, a, b = ellipse_param
elif file_num == 48:
    h, a, b = cir_param


r0_ref_0 = np.array([[x0, y0, z0, hand_open]]).T
r0_ref_1 = calc_r0ref(r0_ref_0, [xf, y0, zf, hand_open], tf, Δ, t)
r0_ref_2 = closeHand(r0_ref_1, tf, Δ, t)
r0_ref_3 = calc_r0ref(r0_ref_2, [x0, y0, z0, hand_close], tf, Δ, t)
r0_ref_4 = calc_r0ref(r0_ref_3, [x0, yf, z0, hand_close], tf, Δ, t)
r0_ref_5 = calc_r0ref(r0_ref_4, [xf, y0, zf, hand_close], tf, Δ, t)
r0_ref_6 = calc_r0ref(r0_ref_5, [xf, y0, z0, hand_close], tf, Δ, t)
r0_ref_7 = calc_r0ref(r0_ref_6, [cir_x0, -a, h+b, hand_close], tf, Δ, t)

if file_num == 47:
    r0_ref_8 = ellipse(
        r0_ref_7, [np.pi*(5/2), np.pi*(1/2), hand_close], cir_tf, cir_Δ, cir_t)
if file_num == 48:
    r0_ref_8 = circle(
        r0_ref_7, [np.pi*(5/2), np.pi*(1/2), hand_close], cir_tf, cir_Δ, cir_t)

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
simulation_3dof(r0_ref, dt, file_num)
