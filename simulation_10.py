import numpy as np
from time import perf_counter
from simulation.simulation_3dof import simulation_3dof
from simulation.軌道生成 import calc_ξ
from simulation.param import *


def main():
    t0, tf, Δ = np.array([0, 0.5, 0.5/4*0.999])
    num = 42
    t, dt = np.linspace(t0, tf, num, retstep=True)

    x0, xf, y0, yf, z0, zf = np.array([170, 170,
                                       0, -50,
                                       150, 150])
    x = calc_ξ(x0, xf, tf, Δ, t)
    y = calc_ξ(y0, yf, tf, Δ, t)
    z = calc_ξ(z0, zf, tf, Δ, t)
    r0_ref = np.array([x, y, z]).T

    t_list = []
    for i in range(1):
        t0 = perf_counter()
        simulation_3dof(r0_ref, dt, 10)
        t1 = perf_counter()
        t_list.append(t1-t0)
    t_ave = np.average(np.array(t_list))
    print(t_ave*1000)


if __name__ == '__main__':
    main()
