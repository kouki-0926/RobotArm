import numpy as np
from simulation.tform_numpy import calc_T2_3dof
from simulation.param import la, lc


def q2r_3dof(q):
    θ1, θ2, θ3 = q
    parm_list = np.array([[0, 0, 0, θ1],
                          [0, -np.pi/2, 0, θ2],
                          [la, 0, 0, θ3],
                          [0, -np.pi/2, lc, 0]])
    return calc_T2_3dof(parm_list)
