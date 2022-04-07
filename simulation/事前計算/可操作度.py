from sympy import *
from tform_sympy import *
from 事前計算_param import *
# ここでの J は手先位置ベクトルが(x, y, z).Tの時のヤコビ行列


def STR(A):
    A = str(A).replace("sin", "np.sin").replace("cos", "np.cos")
    A = A.replace("Abs", "np.abs").replace("(t)", "")
    A = A.replace(" ", "").replace("θ1_2", "q_list[:, 0]")
    A = A.replace("θ1_2", "q_list[p, 0]")
    A = A.replace("θ2_2", "q_list[p, 1]")
    A = A.replace("θ3_2", "q_list[p, 2]").replace("Matrix(", "")
    A = A.replace("],[", "],\n                         [")
    A = A.replace("]])", "]]")
    return A


def calc_w1(dof):
    t = symbols("t", positive=True)
    θ1_2 = Function("θ1_2", real=True)(t)
    θ2_2 = Function("θ2_2", real=True)(t)
    θ3_2 = Function("θ3_2", real=True)(t)
    if (dof == 3 or dof == 32):
        parm_list = parm_list_3dof.subs(θ1, θ1_2).subs(θ2, θ2_2).subs(θ3, θ3_2)

    T03, T_list = calc_T2(parm_list)
    if(dof == 3):
        r0E = trigsimp(T03*r_3dof)
    elif(dof == 32):
        r0E = trigsimp(T03*r_3dof_2)

    J = Matrix([[r0E[i].diff(θ1_2), r0E[i].diff(θ2_2), r0E[i].diff(θ3_2)] for i in range(3)])
    print("    JTJ_list = np.array(["+STR(trigsimp(J.T*J))+" for p in range(num)])")
    # w1 = trigsimp(factor(sqrt((J*J.T).det())))
    # print("    w_list = "+STR(w1))
    # return [J, w1]


if __name__ == '__main__':
    calc_w1(32)

# JvJVt = (Jv*Jv.T).subs(la, 129).subs(lb, 110).subs(lc, 150)
# JvJVt = JvJVt.subs(θ1_2, pi/3).subs(θ2_2, pi/6).subs(θ3_2, pi)
# B = JvJVt.eigenvects()
# λ = Matrix([factor(B[i][0]) for i in range(3)])
# σ = Matrix([sqrt(λ[i]) for i in range(len(λ))])
# p = [[[B[i][2]] for i in range(3)][j][0][0] for j in range(3)]
# print(p[0], σ[0])
# print(p[1], σ[1])
# print(p[2], σ[2])
