import numpy as np


def calcT(parm):
    a, α, d, θ = parm
    T = np.array([[np.cos(θ), -np.sin(θ), 0, a],
                  [np.cos(α)*np.sin(θ), np.cos(α)*np.cos(θ), -np.sin(α), -np.sin(α)*d],
                  [np.sin(α)*np.sin(θ), np.sin(α)*np.cos(θ), np.cos(α), np.cos(α)*d],
                  [0, 0, 0, 1]])
    return T


def calc_T2_3dof(parm_list):
    tmp_T_list = [calcT(parm) for parm in parm_list]
    T01 = tmp_T_list[0]
    T02 = np.dot(T01, tmp_T_list[1])
    T03 = np.dot(T02, tmp_T_list[2])
    T0E = np.dot(T03, tmp_T_list[3])
    return [T01, T02, T03, T0E, tmp_T_list[1], tmp_T_list[2], tmp_T_list[3]]
