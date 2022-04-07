import sys
import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ, calc_t
from simulation.param import *

# ==================================
try:
    file_num = int(sys.argv[1])
except:
    file_num = 49
# ==================================

if file_num == 49:
    tf, Δ, t = calc_t(1.65)
    h, a, b = np.array([92.5, 103.5, 85])
    z0, zf = np.array([170, 170])
elif file_num == 50:
    tf, Δ, t = calc_t(2)
    h, a, b = np.array([90, 90, 85])
    z0, zf = np.array([246, 151])

θ = calc_ξ(0, 2*np.pi, tf, Δ, t)
x = h+a*np.sin(θ)
y = -b+b*np.cos(θ)
z = calc_ξ(z0, zf, tf, Δ, t)
α = calc_ξ(openα, openα, tf, Δ, t)
r0_ref_1 = np.array([x, y, z, α])

r0_ref = np.block([r0_ref_1]).T
simulation_3dof(r0_ref, dt, file_num)
