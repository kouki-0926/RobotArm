# eps=1e-7 の時, 逆運動学が収束
import numpy as np
from time import perf_counter
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *


t0, tf, Δ = np.array([0, 0.85, 0.85/4*0.999])
num = 50
t, dt = np.linspace(t0, tf, num, retstep=True)
stop_step = 3

α = 0.00
β = la+lb-α
l = 0.2910*β
x0, xf, y0, yf, z0, zf = np.array([β-l, β,
                                   0, 0,
                                   np.sqrt(2*l*β-l**2), 0])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_1 = np.array([x, y, z])
r0_ref_1_2 = np.array([r0_ref_1[:, -1] for i in range(stop_step)]).T


x0, xf, y0, yf, z0, zf = np.array([β, β-l,
                                   0, -np.sqrt(2*l*β-l**2),
                                   0, 0])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_2 = np.array([x, y, z])
r0_ref_2_2 = np.array([r0_ref_2[:, -1] for i in range(stop_step)]).T


x0, xf, y0, yf, z0, zf = np.array([β-l, β-l,
                                   -np.sqrt(2*l*β-l**2), 0,
                                   0, np.sqrt(2*l*β-l**2)])
x = calc_ξ(x0, xf, tf, Δ, t)
y = calc_ξ(y0, yf, tf, Δ, t)
z = calc_ξ(z0, zf, tf, Δ, t)
r0_ref_3 = np.array([x, y, z])
r0_ref_3_2 = np.array([r0_ref_3[:, -1] for i in range(stop_step)]).T


r0_ref = np.block([r0_ref_2, r0_ref_2_2,
                   r0_ref_3, r0_ref_3_2,
                   r0_ref_1, r0_ref_1_2]).T

t0 = perf_counter()
simulation_3dof(r0_ref, dt, 9)
t1 = perf_counter()
print(t1-t0)
