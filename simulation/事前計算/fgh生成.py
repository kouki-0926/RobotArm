from sympy import *
from tform_sympy import calc_T2
from 事前計算_param import *


def generate_fgh(parm_list, r):
    T = calc_T2(parm_list)[0]
    r0 = trigsimp(T*r)

    # fgh偏微分生成にコピペ
    # str_r0_1 = [str(r0[i]).replace(" ", "") for i in range(3)]
    # print("    f="+str_r0_1[0]+"-r0x")
    # print("    g="+str_r0_1[1]+"-r0y")
    # print("    h="+str_r0_1[2]+"-r0z")
    return r0


def generate_fgh_2(parm_list, r):
    T = calc_T2(parm_list)[0]
    r0 = trigsimp(T*r)

    # 逆運動学にコピペ
    str_r0_2 = [str(r0[i]).replace(" ", "").replace("cos", "np.cos").replace("sin", "np.sin") for i in range(3)]
    str_r0_2 = [str_r0_2[i].replace("sqrt", "np.sqrt").replace("Abs", "np.abs") for i in range(3)]
    print("        f="+str_r0_2[0]+"-r0x")
    print("        g="+str_r0_2[1]+"-r0y")
    print("        h="+str_r0_2[2]+"-r0z")
    return r0
