import numpy as np
from simulation.simulation_6dof import simulation_6dof
from simulation.param import *


v = 5
n = int(150/v)
n2 = int(90/v)
r0_ref_1 = np.array([[(la+lb)*np.cos(np.deg2rad(-v*p)),
                      (la+lb)*np.sin(np.deg2rad(-v*p)),
                      v*p] for p in range(n)])
r0_ref_2 = np.array([[(la+lb)*np.cos(np.deg2rad(-150+v*p)),
                      (la+lb)*np.sin(np.deg2rad(-150+v*p)),
                      150-2*v*p] for p in range(n)])
r0_ref_3 = np.array([[la+lb+lc*np.sin(np.deg2rad(v*p)),
                      0,
                      -lc*np.cos(np.deg2rad(v*p))] for p in range(n2)])
r0_ref_4 = np.array([[la+(lb+lc)*np.cos(np.deg2rad(v*p)),
                      0,
                      (lb+lc)*np.sin(np.deg2rad(v*p))] for p in range(n2)])
r0_ref_5 = np.array([[la+(lb+lc)*np.cos(np.deg2rad(90-v*p)),
                      0,
                      (lb+lc)*np.sin(np.deg2rad(90-v*p))] for p in range(n2)])
r0_ref_6 = np.array([[la+lb+lc*0.1*(10-p), 0, 0] for p in range(11)])

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
print(r0_ref_5[0])
print("=================== 5-->6 ========================")
print(r0_ref_5[-1])
print(r0_ref_6[0])
print("=================== 6-->7 ========================")
print(r0_ref_6[-1])

r0_ref = np.block([[r0_ref_1],
                   [r0_ref_2],
                   [r0_ref_3],
                   [r0_ref_4],
                   [r0_ref_5],
                   [r0_ref_6]])
simulation_6dof(r0_ref, 1)
