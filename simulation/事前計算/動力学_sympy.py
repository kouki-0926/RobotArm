from inspect import currentframe
from sympy import *


def print2(*args):
    A = str(args[0])
    A = A.replace("Derivative(θ1(t), (t, 2))", "ddq[:,0]")
    A = A.replace("Derivative(θ2(t), (t, 2))", "ddq[:,1]")
    A = A.replace("Derivative(θ3(t), (t, 2))", "ddq[:,2]")

    A = A.replace("Derivative(θ1(t), t)", "dq[:,0]")
    A = A.replace("Derivative(θ2(t), t)", "dq[:,1]")
    A = A.replace("Derivative(θ3(t), t)", "dq[:,2]")

    A = A.replace("θ1(t)", "q[:,0]")
    A = A.replace("θ2(t)", "q[:,1]")
    A = A.replace("θ3(t)", "q[:,2]")

    A = A.replace("sin(", "np.sin(")
    A = A.replace("cos(", "np.cos(")
    A = A.replace(" ", "")
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("        "+", ".join(names.get(id(arg), '???')+" = "+A for arg in args))


def dynamics_sympy(dof):
    t = symbols("t", positive=True)
    θ1 = Function("θ1", real=True)(t)
    θ2 = Function("θ2", real=True)(t)
    θ3 = Function("θ3", real=True)(t)
    dθ1, dθ2, dθ3 = [θ1.diff(t),
                     θ2.diff(t),
                     θ3.diff(t)]

    S1, C1 = [sin(θ1), cos(θ1)]
    S2, C2 = [sin(θ2), cos(θ2)]
    S3, C3 = [sin(θ3), cos(θ3)]
    S12, C12 = [sin(θ1+θ2), cos(θ1+θ2)]
    S23, C23 = [sin(θ2+θ3), cos(θ2+θ3)]

    # ============ 定数 ===========================
    g = 9.81*10**3
    l1, l2, l3 = [50, 129, 110]
    ml, mm = [100, 100]
    I1, I2, I3 = [5e6, 3e7, 6e6]
    # =============================================

    # =============== 3dof ========================
    if(dof == 3):
        m1, m2, m3 = [ml+mm, 2*ml+mm, ml]
        lg1, lg2, lg3 = [(((ml/2)+mm)*l1)/(ml+mm),
                         ((ml+mm)*l2)/(2*ml+mm),
                         (1/2)*l3]
    # =============== 3dof_2 ========================
    if(dof == 32):
        m1, m2, m3 = [ml+mm, 2*ml+mm, ml]
        lg1, lg2, lg3 = [(((ml/2)+mm)*l1)/(ml+mm),
                         ((ml+2*mm)*l2)/(2*(ml+mm)),
                         (1/2)*l3]
    # =============== 6dof ========================
    elif(dof == 6):
        m1, m2, m3 = [ml+mm, 2*ml+mm, ml+2*mm]
        I3 = 2*I3
        lg1, lg2, lg3 = [(((ml/2)+mm)*l1)/(ml+mm),
                         ((ml+mm)*l2)/(2*ml+mm),
                         ((ml+4*mm)*l3)/(2*(ml+2*mm))]
    # =============================================

    xg1 = Matrix([0,
                  0,
                  lg1])
    xg2 = Matrix([lg2*C1*C2,
                  lg2*S1*C2,
                  l1+lg2*S2])
    xg3 = Matrix([l2*C1*C2+lg3*C1*C23,
                  l2*S1*C2+lg3*S1*C23,
                  l1+l2*S2+lg3*S23])

    xg1, xg2, xg3 = [trigsimp(xg1),
                     trigsimp(xg2),
                     trigsimp(xg3)]

    vg1, vg2, vg3 = [trigsimp(xg1.diff(t)),
                     trigsimp(xg2.diff(t)),
                     trigsimp(xg3.diff(t))]

    vg1_2, vg2_2, vg3_2 = [trigsimp(((vg1.T)*vg1)[0]),
                           trigsimp(((vg2.T)*vg2)[0]),
                           trigsimp(((vg3.T)*vg3)[0])]

    K1, K2, K3 = [(1/2)*(m1*vg1_2+I1*dθ1**2),
                  (1/2)*(m2*vg2_2+I2*dθ2**2),
                  (1/2)*(m3*vg3_2+I3*dθ3**2)]
    K = K1+K2+K3

    U1, U2, U3 = [m1*g*xg1[2],
                  m2*g*xg2[2],
                  m3*g*xg3[2]]
    U = simplify(U1+U2+U3)

    L = trigsimp(K-U)
    dL_dθ1, dL_dθ2, dL_dθ3 = [L.diff(θ1),
                              L.diff(θ2),
                              L.diff(θ3)]
    ddL_ddθ1_dt, ddL_ddθ2_dt, ddL_ddθ3_dt = [(L.diff(dθ1)).diff(t),
                                             (L.diff(dθ2)).diff(t),
                                             (L.diff(dθ3)).diff(t)]
    τ = Matrix([simplify(ddL_ddθ1_dt-dL_dθ1),
                simplify(ddL_ddθ2_dt-dL_dθ2),
                simplify(ddL_ddθ3_dt-dL_dθ3)])
    τ1, τ2, τ3 = τ

    print2(τ1)
    print2(τ2)
    print2(τ3)
    return τ


if __name__ == '__main__':
    print("    if(dof == 3):")
    dynamics_sympy(3)
    print("    if(dof == 32):")
    dynamics_sympy(32)
    print("    elif(dof == 6):")
    dynamics_sympy(6)
    print("    return [τ1, τ2, τ3]")
