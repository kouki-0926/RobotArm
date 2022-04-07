import numpy as np
from simulation.param import *


def calc_a(ξ0, dξ0, ddξ0, ξf, dξf, ddξf, tf):
    a0 = ξ0
    a1 = dξ0
    a2 = (1/2)*ddξ0
    a3 = (1/(2*tf**3))*(20*(ξf-ξ0)-(8*dξf+12*dξ0)*tf-(3*ddξ0-ddξf)*tf**2)
    a4 = (1/(2*tf**4))*(30*(ξ0-ξf)+(14*dξf+16*dξ0)*tf+(3*ddξ0-2*ddξf)*tf**2)
    a5 = (1/(2*tf**5))*(12*(ξf-ξ0)-(6*dξf+6*dξ0)*tf-(ddξ0-ddξf)*tf**2)
    return np.array([a0, a1, a2, a3, a4, a5])


def calc_a2(ξ0, dξ0, ddξ0, ξf, dξf, ddξf, tf, t):
    A = calc_a(ξ0, dξ0, ddξ0, ξf, dξf, ddξf, tf)
    anser = A[0]+A[1]*t+A[2]*t**2+A[3]*t**3+A[4]*t**4+A[5]*t**5
    return anser


# Δ < tf/4 が必要
def calc_ξ(ξ0, ξf, tf, Δ, t):
    num = int(Δ/(t[1]-t[0]))
    t_up = t[:2*num+1]
    t_const = t[2*num+1:-(2*num+1)]
    t_down = t[-(2*num+1):]

    slopeOfLine = (ξ0-ξf)/(2*Δ-tf)
    ξ_const = slopeOfLine*(t_const-Δ)+ξ0

    ξ02, ξf1 = np.array([ξ0+slopeOfLine*Δ, ξf-slopeOfLine*Δ])
    ξ_up = calc_a2(ξ0, 0, 0, ξ02, slopeOfLine, 0, 2*Δ, t_up)
    ξ_down = calc_a2(ξf1, slopeOfLine, 0, ξf, 0, 0, 2*Δ, t_down-(tf-2*Δ))
    return np.block([ξ_up, ξ_const, ξ_down])


def calc_t(tf):
    t = np.arange(0, tf, dt)
    Δ = (tf/4)*0.998
    return [tf, Δ, t]


def openHand(pre_ref, tf, Δ, t):
    x = calc_ξ(pre_ref[0, -1], pre_ref[0, -1], tf, Δ, t)
    y = calc_ξ(pre_ref[1, -1], pre_ref[1, -1], tf, Δ, t)
    z = calc_ξ(pre_ref[2, -1], pre_ref[2, -1], tf, Δ, t)
    α = calc_ξ(closeα, openα, tf, Δ, t)
    return np.array([x, y, z, α])


def closeHand(pre_ref, tf, Δ, t):
    x = calc_ξ(pre_ref[0, -1], pre_ref[0, -1], tf, Δ, t)
    y = calc_ξ(pre_ref[1, -1], pre_ref[1, -1], tf, Δ, t)
    z = calc_ξ(pre_ref[2, -1], pre_ref[2, -1], tf, Δ, t)
    α = calc_ξ(openα, closeα, tf, Δ, t)
    return np.array([x, y, z, α])


def constOpenHand(tf, Δ, t):
    return calc_ξ(openα, openα, tf, Δ, t)


def constCloseHand(tf, Δ, t):
    return calc_ξ(closeα, closeα, tf, Δ, t)


def calc_r0ref(pre_ref, r_ref, tf, Δ, t):
    x0, y0, z0, α0 = pre_ref[:, -1]
    xf, yf, zf, handState = r_ref

    x = calc_ξ(x0, xf, tf, Δ, t)
    y = calc_ξ(y0, yf, tf, Δ, t)
    z = calc_ξ(z0, zf, tf, Δ, t)
    if(handState == hand_open):
        α = calc_ξ(α0, openα, tf, Δ, t)
    if(handState == hand_close):
        α = calc_ξ(α0, closeα, tf, Δ, t)
    return np.array([x, y, z, α])


def common_circle(pre_ref, r_ref, tf, Δ, t, h, a, b):
    α0 = pre_ref[3, -1]
    θ0, θf, handState = r_ref

    θ = calc_ξ(θ0, θf, tf, Δ, t)
    x = calc_ξ(cir_x0, cir_x0, tf, Δ, t)
    y = -a-a*np.cos(θ)
    z = h+b*np.sin(θ)
    if(handState == hand_open):
        α = calc_ξ(α0, openα, tf, Δ, t)
    if(handState == hand_close):
        α = calc_ξ(α0, closeα, tf, Δ, t)
    return np.array([x, y, z, α])


def circle(pre_ref, r_ref, cir_tf, cir_Δ, cir_t):
    h, a, b = cir_param
    return common_circle(pre_ref, r_ref, cir_tf, cir_Δ, cir_t, h, a, b)


def ellipse(pre_ref, r_ref, cir_tf, cir_Δ, cir_t):
    h, a, b = ellipse_param
    return common_circle(pre_ref, r_ref, cir_tf, cir_Δ, cir_t, h, a, b)


def ellipse2(pre_ref, r_ref, cir_tf, cir_Δ, cir_t):
    h, a, b = ellipse2_param
    return common_circle(pre_ref, r_ref, cir_tf, cir_Δ, cir_t, h, a, b)
