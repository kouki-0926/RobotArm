import numpy as np
from simulation.simulation_6dof import simulation_6dof
from simulation.param import *

v = 1
n = int(90/v)
r0_ref_1 = np.array([[la+lb+lc*np.sin(np.deg2rad(v*p)),
                      0,
                      -lc*np.cos(np.deg2rad(v*p))] for p in range(n+1)])

print(r0_ref_1[0])
print("=================== 1-->2 ========================")
print(r0_ref_1[-1])

r0_ref = np.block([[r0_ref_1]])
simulation_6dof(r0_ref, 3)
