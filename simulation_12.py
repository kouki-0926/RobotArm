import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.param import *

r0_ref_1 = np.array([[(la+lb-10)*np.cos(np.deg2rad(p)),
                    0,
                    (la+lb-10)*np.sin(np.deg2rad(p))]
    for p in range(155)])
r0_ref_2 = np.array([[(la+lb-10)*np.cos(np.deg2rad(p)),
                    0,
                    (la+lb-10)*np.sin(np.deg2rad(p))]
    for p in range(155, 0, -1)])

r0_ref = np.block([[r0_ref_1],
                   [r0_ref_2]])
dt = 0.01
simulation_3dof(r0_ref, dt, 12)
