import numpy as np
from simulation.simulation_6dof import simulation_6dof
from simulation.param import *

r0_ref_1 = np.array([[la+lb+lc*np.sin(np.deg2rad(p)),
                      0,
                      -lc*np.cos(np.deg2rad(p))] for p in range(90)])
r0_ref_2 = np.array([[la+(lb+lc)*np.cos(np.deg2rad(p)),
                      0,
                      (lb+lc)*np.sin(np.deg2rad(p))] for p in range(90)])
r0_ref_3 = np.array([[la+(lb+lc)*np.cos(np.deg2rad(90-p)),
                      0,
                      (lb+lc)*np.sin(np.deg2rad(90-p))] for p in range(90)])
r0_ref_4 = np.array([[la+lb+lc*np.sin(np.deg2rad(90-p)),
                      0,
                      -lc*np.cos(np.deg2rad(90-p))] for p in range(90)])

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
simulation_6dof(r0_ref, 2)
