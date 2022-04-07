import numpy as np
from simulation.tform_numpy import calc_T2_3dof, calc_T2_6dof
from simulation.param import la, lb, lc


def q2r_3dof(q):
    θ1, θ2, θ3 = q
    parm_list = np.array([[0, 0, 0, θ1],
                          [0, -np.pi/2, 0, θ2],
                          [la, 0, 0, θ3],
                          [0, -np.pi/2, lc, 0]])
    return calc_T2_3dof(parm_list)


def q2r_6dof(q):
    θ1, θ2, θ3, θ4, θ5 = q

    parm_list = np.array([[0, 0, 0, θ1],
                          [0, -np.pi/2, 0, θ2],
                          [la, 0, 0, θ3],
                          [lb, 0, 0, θ4],
                          [0, -np.pi/2, 0, θ5]])
    T01, T02, T03, T04, T05 = calc_T2_6dof(parm_list)
    r5E = np.array([0, 0, lc, 1])
    r0E = np.dot(T05, r5E)
    return [r0E, T01, T02, T03, T04, T05]
