import numpy as np
from simulation.param import la, lb, lc


def calc_manipulability(q_list, num):
    JTJ_list = np.array([[[(la*np.cos(q_list[p, 1])-lc*np.sin(q_list[p, 1]+q_list[p, 2]))**2, 0, 0],
                          [0, la**2-2*la*lc*np.sin(q_list[p, 2])+lc**2, lc*(-la*np.sin(q_list[p, 2])+lc)],
                          [0, lc*(-la*np.sin(q_list[p, 2])+lc), lc**2]] for p in range(num)])
    detM = 1.297998e+21*(3.94453612409264e-19*np.cos(q_list[:,0])**4*np.cos(q_list[:,1])**2*np.cos(q_list[:,1]+q_list[:,2])**3*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])-1.57781444963706e-18*np.cos(q_list[:,0])**4*np.cos(q_list[:,1])**2*np.cos(q_list[:,1]+q_list[:,2])**2*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])**2-4.9306701551158e-20*np.cos(q_list[:,0])**4*np.cos(q_list[:,1])*np.cos(q_list[:,1]+q_list[:,2])**4*np.sin(q_list[:,0])**2*np.sin(q_list[:,1]+q_list[:,2])-3.15562889927411e-18*np.cos(q_list[:,0])**4*np.cos(q_list[:,1])*np.cos(q_list[:,1]+q_list[:,2])**2*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])**2*np.sin(q_list[:,1]+q_list[:,2])-6.16333769389475e-21*np.cos(q_list[:,0])**4*np.cos(q_list[:,1]+q_list[:,2])**4*np.sin(q_list[:,0])**2*np.sin(q_list[:,1]+q_list[:,2])**2-4.9306701551158e-20*np.cos(q_list[:,0])**4*np.cos(q_list[:,1]+q_list[:,2])**3*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])*np.sin(q_list[:,1]+q_list[:,2])**2+2.36672167445558e-18*np.cos(q_list[:,0])**4*np.cos(q_list[:,1]+q_list[:,2])**3*np.sin(q_list[:,1])-4.9306701551158e-20*np.cos(q_list[:,0])**4*np.cos(q_list[:,1]+q_list[:,2])**2*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])**2*np.sin(q_list[:,1]+q_list[:,2])**2+0.00230769230769231*np.cos(q_list[:,0])**4*np.cos(q_list[:,1]+q_list[:,2])**2*np.sin(q_list[:,1])**2+0.0166153846153847*np.cos(q_list[:,0])**2*np.cos(q_list[:,1])**2*np.cos(q_list[:,1]+q_list[:,2])**2*np.sin(q_list[:,0])**2+7.57350935825787e-17*np.cos(q_list[:,0])**2*np.cos(q_list[:,1])**2*np.cos(q_list[:,1]+q_list[:,2])*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])-5.99569490862081e-17*np.cos(q_list[:,0])**2*np.cos(q_list[:,1])*np.cos(q_list[:,1]+q_list[:,2])**2*np.sin(q_list[:,0])**2*np.sin(q_list[:,1]+q_list[:,2])+0.00553846153846145*np.cos(q_list[:,0])**2*np.cos(q_list[:,1])*np.cos(q_list[:,1]+q_list[:,2])*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])*np.sin(q_list[:,1]+q_list[:,2])-1.13602640373868e-16*np.cos(q_list[:,0])**2*np.cos(q_list[:,1])*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])**2*np.sin(q_list[:,1]+q_list[:,2])+0.0374422764904107*np.cos(q_list[:,0])**2*np.cos(q_list[:,1]+q_list[:,2])**2-7.88907224818528e-19*np.cos(q_list[:,0])**2*np.cos(q_list[:,1]+q_list[:,2])*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])*np.sin(q_list[:,1]+q_list[:,2])**2+0.0536672629695885*np.cos(q_list[:,0])**2*np.cos(q_list[:,1]+q_list[:,2])*np.sin(q_list[:,1])+0.00276923076923075*np.cos(q_list[:,0])**2*np.sin(q_list[:,0])**2*np.sin(q_list[:,1])**2*np.sin(q_list[:,1]+q_list[:,2])**2+0.166666666666666*np.cos(q_list[:,0])**2*np.sin(q_list[:,1])**2+1.0*np.cos(q_list[:,1])**2*np.sin(q_list[:,0])**2-0.322003577817532*np.cos(q_list[:,1])*np.sin(q_list[:,0])**2*np.sin(q_list[:,1]+q_list[:,2])+0.0374422764904106*np.sin(q_list[:,0])**2*np.sin(q_list[:,1]+q_list[:,2])**2+0.69337549056316)

    σ_list = np.array([np.sort(np.sqrt(np.linalg.eig(JTJ)[0])) for JTJ in JTJ_list])

    w1_list = np.prod(σ_list, axis=1)
    w2_list = σ_list[:, 0]/σ_list[:, 2]
    w3_list = σ_list[:, 0]
    w4_list = w1_list**(1/3)
    wd_list = w1_list/detM
    return np.array([w1_list, w2_list, w3_list, w4_list, wd_list])
