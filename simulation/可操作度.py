import numpy as np
from simulation.param import la, lb, lc


def calc_manipulability(q_list, num):
    JTJ_list = np.array([[[(la*np.cos(q_list[p, 1])-lc*np.sin(q_list[p, 1]+q_list[p, 2]))**2, 0, 0],
                          [0, la**2-2*la*lc*np.sin(q_list[p, 2])+lc**2, lc*(-la*np.sin(q_list[p, 2])+lc)],
                          [0, lc*(-la*np.sin(q_list[p, 2])+lc), lc**2]] for p in range(num)])

    σ_list = np.array([np.sort(np.sqrt(np.linalg.eig(JTJ)[0])) for JTJ in JTJ_list])

    w1_list = np.prod(σ_list, axis=1)
    w2_list = σ_list[:, 0]/σ_list[:, 2]
    w3_list = σ_list[:, 0]
    w4_list = w1_list**(1/3)
    return np.array([w1_list, w2_list, w3_list, w4_list])
