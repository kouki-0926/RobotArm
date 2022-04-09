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
    print("    "+", ".join(names.get(id(arg), '???')+" = "+A for arg in args))


def print3(*args):
    A = str(trigsimp(args[0]))
    A = A.replace("Derivative(θ1(t), (t, 2))", "ddθ1")
    A = A.replace("Derivative(θ2(t), (t, 2))", "ddθ2")
    A = A.replace("Derivative(θ3(t), (t, 2))", "ddθ3")

    A = A.replace("Derivative(θ1(t), t)", "dθ1")
    A = A.replace("Derivative(θ2(t), t)", "dθ2")
    A = A.replace("Derivative(θ3(t), t)", "dθ3")

    A = A.replace("θ1(t)", "θ1")
    A = A.replace("θ2(t)", "θ2")
    A = A.replace("θ3(t)", "θ3")

    A = A.replace(" ", "")
    A = A.replace("1.0*", "")

    A = A.replace("sin(θ1)", "S1")
    A = A.replace("sin(θ2)", "S2")
    A = A.replace("sin(θ3)", "S3")

    A = A.replace("cos(θ1)", "C1")
    A = A.replace("cos(θ2)", "C2")
    A = A.replace("cos(θ3)", "C3")

    A = A.replace("sin(θ2+θ3)", "S23")
    A = A.replace("cos(θ2+θ3)", "C23")
    A = A.replace("cos(2*(θ1-θ2))-cos(2*(θ1+θ2))", "8*S1*S2*C1*C2")
    A = A.replace("cos(2*(-θ1+θ2+θ3))-cos(2*(θ1+θ2+θ3))", "8*S1*S23*C1*C23")

    A = factor(simplify(A))
    A = str(A)

    A = A.replace(" ", "")
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print(", ".join(names.get(id(arg), '???')+" = "+A for arg in args))


def dynamics_sympy():
    t = symbols("t", positive=True)
    θ1 = Function("θ1", real=True)(t)
    θ2 = Function("θ2", real=True)(t)
    θ3 = Function("θ3", real=True)(t)
    dθ1, dθ2, dθ3 = [θ1.diff(t),
                     θ2.diff(t),
                     θ3.diff(t)]

    # ============ 定数 ===========================
    g = 9.81*10**3
    la, lb, lc, ld = [129, 110, 150, 105]
    ml, mm, mh = [100, 100, 100]
    I1, I2, I3 = [5e6, 3e7, 6e6]
    # =============================================

    m1, m2, m3 = [ml+mm, 2*ml+mm, mh+2*mm]
    l1, l2 = [10, 20]
    lg1, lg2, lg3 = [l1,
                     ((ml+mm)/(2*ml+mm))*la,
                     ((1/3)*lc*mh+2*mm*l2)/(mh+2*mm)]

    # m1, m2, m3, g = symbols("m1, m2, m3, g", positive=True)
    # I1, I2, I3 = symbols("I1, I2, I3", positive=True)
    # lg1, lg2, lg3 = symbols("lg1, lg2, lg3", positive=True)
    # la, lb, lc, ld = symbols("la, lb, lc, ld", positive=True)

    xg1 = Matrix([0,
                  -lg1,
                  0])
    xg2 = Matrix([[lg2*cos(θ1)*cos(θ2),
                   lg2*sin(θ1)*cos(θ2),
                   -lg2*sin(θ2)]])
    xg3 = Matrix([[(la*cos(θ2)-lg3*sin(θ2+θ3))*cos(θ1),
                   (la*cos(θ2)-lg3*sin(θ2+θ3))*sin(θ1),
                   -la*sin(θ2)-lg3*cos(θ2+θ3)]])

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

    print3(τ1)
    print3(τ2)
    print3(τ3)
    # print("    return np.array([τ1, τ2, τ3])")
    return τ


if __name__ == '__main__':
    dynamics_sympy()
