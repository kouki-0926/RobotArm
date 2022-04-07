import numpy as np


def generatOrbit_6dof(r0):
    eps = 1e-10
    la, lb, lc, ld = np.array([129, 110, 150, 105])
    r0x, r0y, r0z = r0
    θ1 = np.arctan2(r0y, r0x)
    θ2, θ3, θ4 = np.deg2rad(np.array([-70, 0, -90]))
    Δθ2, Δθ3, Δθ4 = np.array([1, 1, 1])

    while(np.max(np.abs(np.array([Δθ2, Δθ3, Δθ4]))) > eps):
        f = (la*np.cos(θ2)+lb*np.cos(θ2+θ3)-lc*np.sin(θ2+θ3+θ4))*np.cos(θ1)-r0x
        g = (la*np.cos(θ2)+lb*np.cos(θ2+θ3)-lc*np.sin(θ2+θ3+θ4))*np.sin(θ1)-r0y
        h = -la*np.sin(θ2)-lb*np.sin(θ2+θ3)-lc*np.cos(θ2+θ3+θ4)-r0z

        fθ2 = -(la*np.sin(θ2)+lb*np.sin(θ2+θ3)+lc*np.cos(θ2+θ3+θ4))*np.cos(θ1)
        fθ3 = -(lb*np.sin(θ2+θ3)+lc*np.cos(θ2+θ3+θ4))*np.cos(θ1)
        fθ4 = -lc*np.cos(θ1)*np.cos(θ2+θ3+θ4)
        gθ2 = -(la*np.sin(θ2)+lb*np.sin(θ2+θ3)+lc*np.cos(θ2+θ3+θ4))*np.sin(θ1)
        gθ3 = -(lb*np.sin(θ2+θ3)+lc*np.cos(θ2+θ3+θ4))*np.sin(θ1)
        gθ4 = -lc*np.sin(θ1)*np.cos(θ2+θ3+θ4)
        hθ2 = -la*np.cos(θ2)-lb*np.cos(θ2+θ3)+lc*np.sin(θ2+θ3+θ4)
        hθ3 = -lb*np.cos(θ2+θ3)+lc*np.sin(θ2+θ3+θ4)
        hθ4 = lc*np.sin(θ2+θ3+θ4)
        A = [[fθ2, fθ3, fθ4],
             [gθ2, gθ3, gθ4],
             [hθ2, hθ3, hθ4]]
        b = [-f, -g, -h]
        A_inv = np.linalg.pinv(A)

        Δθ2, Δθ3, Δθ4 = np.dot(A_inv, b)
        θ2, θ3, θ4 = np.array([θ2+Δθ2, θ3+Δθ3, θ4+Δθ4])

        # 機構上の制限は -155 < θ2 < 0
        if(θ2 <= np.deg2rad(-155)):
            # θ2 += 2*np.pi
            θ2 = np.deg2rad(-155)
        elif(θ2 >= 0):
            θ2 = 0

        # 機構上の制限は -90 < θ3 < 90
        if(θ3 <= -np.pi/2):
            θ3 = -np.pi/2
        elif(θ3 >= np.pi/2):
            θ3 = np.pi/2

        # 機構上の制限は -180 < θ4 < 0
        if(θ4 <= -np.pi):
            θ4 = -np.pi
        elif(θ4 >= 0):
            θ4 = 0
    return np.array([θ1, θ2, θ3, θ4])


if __name__ == '__main__':
    r0 = np.array([239, 0, 0])
    q = generatOrbit_6dof(r0)
    print(q)
