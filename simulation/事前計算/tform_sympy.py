from sympy import *


def calcT(parm):
    a, α, d, θ = parm
    T = Matrix([[cos(θ), -sin(θ), 0, a],
                [cos(α)*sin(θ), cos(α)*cos(θ), -sin(α), -sin(α)*d],
                [sin(α)*sin(θ), sin(α)*cos(θ), cos(α), cos(α)*d],
                [0, 0, 0, 1]])
    return T


def calc_T2(parm_list):
    T_list = [calcT(parm_list.row(i)) for i in range(parm_list.shape[0])]
    T = eye(4)
    for i in range(len(T_list)):
        T = T*T_list[i]
    return [T, T_list]
