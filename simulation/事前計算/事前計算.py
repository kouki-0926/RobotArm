from fgh生成 import generate_fgh_2
from fgh偏微分生成 import generate_dfgh
from 事前計算_param import *
from tform_sympy import calc_T2


def pre_calc(dof):
    if(dof == 3):
        f, g, h = generate_fgh_2(parm_list_3dof, r_3dof)[0:3]
    elif(dof == 32):
        f, g, h = generate_fgh_2(parm_list_3dof, r_3dof_2)[0:3]
    elif(dof == 6):
        f, g, h = generate_fgh_2(parm_list_6dof, r_6dof)[0:3]

    generate_dfgh(f, g, h, dof)


def print2(A):
    A = str(A).replace(" ", "").replace(",", ",\n                    ")
    print("    xg2 = Matrix(["+A+"])")


if __name__ == '__main__':
    pre_calc(32)

    # lg1, lg2, lg3 = symbols("lg1, lg2, lg3")

    # xg2 = calc_T2(parm_list_3dof[0:2, :])[0]*Matrix([lg2, 0, 0, 1])
    # print2(trigsimp(xg2)[0:3])
    # xg3 = calc_T2(parm_list_3dof[0: 3, :])[0]*Matrix([0, lg3, 0, 1])
    # print2(trigsimp(xg3)[0:3])
