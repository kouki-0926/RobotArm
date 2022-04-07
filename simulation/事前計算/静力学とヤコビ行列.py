from tform_sympy import calcT, calc_T2
from 動力学_sympy import dynamics_sympy
from 事前計算_param import *
from sympy import *
from inspect import currentframe


def print2(*args):
    A = str(args[0])
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
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("        "+", ".join(names.get(id(arg), '???')+" = "+A for arg in args))
    return simplify(A)


parm_list = parm_list_3dof
r3E = r_3dof_2
la2, lb2, lc2, ld2 = [129, 110, 150, 105]

# ===================== Jv =====================
T01, T12, T23 = calc_T2(parm_list)[1]
T02 = T01*T12
T03 = T02*T23

z01 = T01[0:3, 2]
z02 = T02[0:3, 2]
z03 = T03[0:3, 2]

p0E = Matrix((T03*r3E)[0:3])
p01 = T01[:3, 3]
p02 = T02[:3, 3]
p03 = T03[:3, 3]

p0E1 = p0E-p01
p0E2 = p0E-p02
p0E3 = p0E-p03

Jv = Matrix([[z01.cross(p0E1), z02.cross(p0E2), z03.cross(p0E3)],
             [z01, z02, z03]])
Jv = Jv.subs(la, la2).subs(lb, lb2).subs(lc, lc2)
print(Jv)
# ===================== end Jv =====================

# τ = dynamics_sympy(32)
# τ = print2(τ)

# T3E = calcT(Matrix([0, -pi/2, lc, 0]))

# T0E = trigsimp(T03*T3E)
# R0E = T0E[0:3, 0:3]


# JvT_pinv = trigsimp((trigsimp(trigsimp(Jv*Jv.T).inv()))*Jv)
# pprint(JvT_pinv.shape)

# R0E_inv = trigsimp(R0E.inv())
# pprint(R0E_inv)

# fnEE = R0E_inv*JvT_pinv*τ
# pprint(fnEE)
