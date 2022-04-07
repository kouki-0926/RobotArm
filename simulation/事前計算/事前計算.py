from fgh生成 import generate_fgh_2
from fgh偏微分生成 import generate_dfgh
from 事前計算_param import *


def pre_calc(dof):
    if(dof == 3):
        f, g, h = generate_fgh_2(parm_list_3dof, r_3dof)[0:3]
    elif(dof == 32):
        f, g, h = generate_fgh_2(parm_list_3dof, r_3dof_2)[0:3]
    elif(dof == 6):
        f, g, h = generate_fgh_2(parm_list_6dof, r_6dof)[0:3]

    generate_dfgh(f, g, h, dof)


if __name__ == '__main__':
    pre_calc(32)
