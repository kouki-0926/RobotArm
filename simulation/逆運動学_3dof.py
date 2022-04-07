import numpy as np


def generatOrbit_3dof(r0):
    eps = 1e-10
    la, lb, lc, ld = np.array([129, 110, 150, 105])
    r0x, r0y, r0z = r0
    θ1, θ2, θ3 = np.deg2rad(np.array([0, -70, 0]))
    Δθ1, Δθ2, Δθ3 = np.array([1, 1, 1])

    while(np.max(np.abs(np.array([Δθ1, Δθ2, Δθ3]))) > eps):
        f = (la*np.cos(θ2)-lc*np.sin(θ2+θ3))*np.cos(θ1)-r0x
        g = (la*np.cos(θ2)-lc*np.sin(θ2+θ3))*np.sin(θ1)-r0y
        h = -la*np.sin(θ2)-lc*np.cos(θ2+θ3)-r0z

        fθ1 = -(la*np.cos(θ2)-lc*np.sin(θ2+θ3))*np.sin(θ1)
        fθ2 = -(la*np.sin(θ2)+lc*np.cos(θ2+θ3))*np.cos(θ1)
        fθ3 = -lc*np.cos(θ1)*np.cos(θ2+θ3)
        gθ1 = (la*np.cos(θ2)-lc*np.sin(θ2+θ3))*np.cos(θ1)
        gθ2 = -(la*np.sin(θ2)+lc*np.cos(θ2+θ3))*np.sin(θ1)
        gθ3 = -lc*np.sin(θ1)*np.cos(θ2+θ3)
        hθ1 = 0
        hθ2 = -la*np.cos(θ2)+lc*np.sin(θ2+θ3)
        hθ3 = lc*np.sin(θ2+θ3)
        A = [[fθ1, fθ2, fθ3],
             [gθ1, gθ2, gθ3],
             [hθ1, hθ2, hθ3]]
        b = [-f, -g, -h]
        A_inv = np.linalg.pinv(A)

        Δθ1, Δθ2, Δθ3 = np.dot(A_inv, b)
        θ1, θ2, θ3 = np.array([θ1+Δθ1, θ2+Δθ2, θ3+Δθ3])

        # 機構上の制限は -146 < θ1 < 0
        if(θ1 <= np.deg2rad(-146)):
            θ1 = np.deg2rad(-146)
        elif(θ1 >= 0):
            θ1 = 0

        # 機構上の制限は -155 < θ2 < 0
        if(θ2 <= np.deg2rad(-155)):
            θ2 += 2*np.pi
            # θ2 = np.deg2rad(-155)
        elif(θ2 >= 0):
            θ2 = 0

        # 機構上の制限は -90 < θ3 < 90
        if(θ3 <= -np.pi/2):
            θ3 = -np.pi/2
        elif(θ3 >= np.pi/2):
            θ3 = np.pi/2
    return np.array([θ1, θ2, θ3])


if __name__ == '__main__':
    import time

    t_list = []
    for i in range(100):
        start_time = time.perf_counter()

        r = np.array([150, 0, i]).T
        generatOrbit_3dof(r)

        end_time = time.perf_counter()
        t_list.append((end_time-start_time)*1000)
    ave_t = np.average(np.array(t_list))
    print(ave_t)
