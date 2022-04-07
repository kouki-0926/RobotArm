import numpy as np
from simulation.軌道生成 import calc_ξ
from simulation.simulation_6dof import simulation_6dof
from simulation.param import *

t0, tf, Δ = np.array([0, 0.5, 0.124])
θ0, θf = np.array([0, 90])
num = 10
t = np.arange(t0, tf+Δ/num, Δ/num)
θ = calc_ξ(θ0, θf, tf, Δ, t)

r0_ref = np.array([la+(lb+lc)*np.cos(np.deg2rad(θ)),
                   np.zeros(θ.shape),
                   (lb+lc)*np.sin(np.deg2rad(θ))]).T

simulation_6dof(r0_ref, 5)
