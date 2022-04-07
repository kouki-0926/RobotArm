# 逆運動学の制限が θ2 > 0.1 の時収束
import numpy as np
from simulation.simulation_6dof import simulation_6dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *


t0, tf, Δ = np.array([0, 0.5, 0.124])
θ0, θf = np.array([0, 90])
num = 10
t = np.arange(t0, tf+Δ/num, Δ/num)
θ = calc_ξ(θ0, θf, tf, Δ, t)

n = θ.shape
r0_ref_1 = np.array([la+lb+lc*np.sin(np.deg2rad(θ)),
                     np.zeros(n),
                     -lc*np.cos(np.deg2rad(θ))]).T
r0_ref_2 = np.array([la+(lb+lc)*np.cos(np.deg2rad(θ)),
                     np.zeros(n),
                     (lb+lc)*np.sin(np.deg2rad(θ))]).T
r0_ref_3 = np.array([la+(lb+lc)*np.cos(np.deg2rad(90-θ)),
                     np.zeros(n),
                     (lb+lc)*np.sin(np.deg2rad(90-θ))]).T
r0_ref_4 = np.array([la+lb+lc*np.sin(np.deg2rad(90-θ)),
                     np.zeros(n),
                     -lc*np.cos(np.deg2rad(90-θ))]).T

print(r0_ref_1[0])
print("=================== 1-->2 ========================")
print(r0_ref_1[-1])
print(r0_ref_2[0])
print("=================== 2-->3 ========================")
print(r0_ref_2[-1])
print(r0_ref_3[0])
print("=================== 3-->4 ========================")
print(r0_ref_3[-1])
print(r0_ref_4[0])
print("=================== 4-->5 ========================")
print(r0_ref_4[-1])

r0_ref = np.block([[r0_ref_1],
                   [r0_ref_2],
                   [r0_ref_3],
                   [r0_ref_4]])
simulation_6dof(r0_ref, "2_2")
