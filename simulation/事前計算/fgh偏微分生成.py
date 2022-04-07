from sympy import *
from 事前計算_param import *


def STR(A):
    return str(A).replace(" ", "").replace("cos", "np.cos").replace("sin", "np.sin").replace("sqrt", "np.sqrt")


def generate_dfgh(f, g, h, dof):
    # 逆運動学にコピペ
    # print("        f = "+STR(f))
    # print("        g = "+STR(g))
    # print("        h = "+STR(h))
    print("")

    fθ1 = trigsimp(f.diff(θ1))
    fθ2 = trigsimp(f.diff(θ2))
    fθ3 = trigsimp(f.diff(θ3))
    fθ4 = trigsimp(f.diff(θ4))
    if(dof == 3 or dof == 32):
        print("        fθ1 = "+STR(fθ1))
    print("        fθ2 = "+STR(fθ2))
    print("        fθ3 = "+STR(fθ3))
    if(dof == 6):
        print("        fθ4 = "+STR(fθ4))

    gθ1 = trigsimp(g.diff(θ1))
    gθ2 = trigsimp(g.diff(θ2))
    gθ3 = trigsimp(g.diff(θ3))
    gθ4 = trigsimp(g.diff(θ4))
    if(dof == 3 or dof == 32):
        print("        gθ1 = "+STR(gθ1))
    print("        gθ2 = "+STR(gθ2))
    print("        gθ3 = "+STR(gθ3))
    if(dof == 6):
        print("        gθ4 = "+STR(gθ4))

    hθ1 = trigsimp(h.diff(θ1))
    hθ2 = trigsimp(h.diff(θ2))
    hθ3 = trigsimp(h.diff(θ3))
    hθ4 = trigsimp(h.diff(θ4))
    if(dof == 3 or dof == 32):
        print("        hθ1 = "+STR(hθ1))
    print("        hθ2 = "+STR(hθ2))
    print("        hθ3 = "+STR(hθ3))
    if(dof == 6):
        print("        hθ4 = "+STR(hθ4))
