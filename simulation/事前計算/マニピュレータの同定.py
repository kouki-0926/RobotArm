from sympy import *
from 動力学_sympy import dynamics_sympy


def replace2(*args):
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

    A = A.replace("I1", "(φ17-φ11*lg1**2)")
    A = A.replace("I2", "(φ27-φ21*lg2**2)")
    A = A.replace("I3", "(φ37-φ31*lg3**2)")

    A = A.replace("lg1", "(-φ14/m1)")
    A = A.replace("lg2", "(φ22/m2)")
    A = A.replace("lg3", "(φ33/m3)")

    A = A.replace("m1", "φ11")
    A = A.replace("m2", "φ21")
    A = A.replace("m3", "φ31")
    return simplify(A)


def print2(A):
    A = str(factor(A))
    A = A.replace(" ", "")

    A = A.replace("S23", "np.sin(q_list[:,1]+q_list[:,2])")
    A = A.replace("C23", "np.cos(q_list[:,1]+q_list[:,2])")

    A = A.replace("S1", "np.sin(q_list[:,0])")
    A = A.replace("S2", "np.sin(q_list[:,1])")
    A = A.replace("S3", "np.sin(q_list[:,2])")
    A = A.replace("C1", "np.cos(q_list[:,0])")
    A = A.replace("C2", "np.cos(q_list[:,1])")
    A = A.replace("C3", "np.cos(q_list[:,2])")
    print("    detM = "+A)


m1, m2, m3, g = symbols("m1, m2, m3, g", positive=True)
I1, I2, I3 = symbols("I1, I2, I3", positive=True)
lg1, lg2, lg3 = symbols("lg1, lg2, lg3", positive=True)
la, lb, lc, ld = symbols("la, lb, lc, ld", positive=True)
θ1, θ2, θ3 = symbols("θ1, θ2, θ3", real=True)
dθ1, dθ2, dθ3 = symbols("dθ1, dθ2, dθ3", real=True)
ddθ1, ddθ2, ddθ3 = symbols("ddθ1, ddθ2, ddθ3", real=True)

S1, S2, S3, C1, C2, C3, S23, C23 = symbols("S1, S2, S3, C1, C2, C3, S23, C23", real=True)
# S1, S2, S3 = [sin(θ1), sin(θ2), sin(θ3)]
# C1, C2, C3 = [cos(θ1), cos(θ2), cos(θ3)]
# S23, C23 = [sin(θ2+θ3), cos(θ2+θ3)]

τ1 = 14422200.0*(0.5*C1*C2**2*S1*dθ1**2+0.5*C1*C2**2*S1*dθ2**2+0.0805008944543828*C1*C2*C23*S1*ddθ2+0.0805008944543828*C1*C2*C23*S1*ddθ3+0.5*C1*C2*S1*S2*ddθ2-0.161001788908766*C1*C2*S1*S23*dθ1**2-0.161001788908766*C1*C2*S1*S23*dθ2**2-0.161001788908766*C1*C2*S1*S23*dθ2*dθ3-0.0805008944543828*C1*C2*S1*S23*dθ3**2-0.0187211382452053*C1*C23*S1*S23*ddθ2-0.0187211382452053*C1*C23*S1*S23*ddθ3-0.0805008944543828*C1*S1*S2*S23*ddθ2+0.0187211382452053*C1*S1*S23**2*dθ1**2+0.0187211382452053*C1*S1*S23**2*dθ2**2+0.0374422764904106*C1*S1*S23**2*dθ2*dθ3+0.0187211382452053*C1*S1*S23**2*dθ3**2+0.5*C2**2*S1**2*ddθ1-0.161001788908766*C2*C23*S1**2*dθ1*dθ2-0.161001788908766*C2*C23*S1**2*dθ1*dθ3-1.0*C2*S1**2*S2*dθ1*dθ2-0.161001788908766*C2*S1**2*S23*ddθ1+0.0374422764904106*C23*S1**2*S23*dθ1*dθ2+0.0374422764904106*C23*S1**2*S23*dθ1*dθ3+0.161001788908766*S1**2*S2*S23*dθ1*dθ2+0.0187211382452053*S1**2*S23**2*ddθ1+0.34668774528158*ddθ1)
τ2 = 632745000.0*(0.0018348623853211*C1**2*C2*C23*dθ1**2+0.0018348623853211*C1**2*C2*C23*dθ2**2+0.0113965341488277*C1**2*C2*S2*dθ1**2+0.0113965341488277*C1**2*C2*S2*dθ2**2+0.000426712182632814*C1**2*C23**2*ddθ2+0.000426712182632814*C1**2*C23**2*ddθ3+0.0036697247706422*C1**2*C23*S2*ddθ2+0.0018348623853211*C1**2*C23*S2*ddθ3-0.000426712182632814*C1**2*C23*S23*dθ1**2-0.000426712182632814*C1**2*C23*S23*dθ2**2-0.000853424365265628*C1**2*C23*S23*dθ2*dθ3-0.000426712182632814*C1**2*C23*S23*dθ3**2+0.0113965341488277*C1**2*S2**2*ddθ2-0.0018348623853211*C1**2*S2*S23*dθ1**2-0.0018348623853211*C1**2*S2*S23*dθ2**2-0.0036697247706422*C1**2*S2*S23*dθ2*dθ3-0.0018348623853211*C1**2*S2*S23*dθ3**2+0.0018348623853211*C1*C2*C23*S1*ddθ1+0.0113965341488277*C1*C2*S1*S2*ddθ1-0.000853424365265628*C1*C23**2*S1*dθ1*dθ2-0.000853424365265628*C1*C23**2*S1*dθ1*dθ3-0.0073394495412844*C1*C23*S1*S2*dθ1*dθ2-0.0036697247706422*C1*C23*S1*S2*dθ1*dθ3-0.000426712182632814*C1*C23*S1*S23*ddθ1-0.0227930682976555*C1*S1*S2**2*dθ1*dθ2-0.0018348623853211*C1*S1*S2*S23*ddθ1-1.0*C2+0.13953488372093*S23+0.0474124647369794*ddθ2)
τ3 = 88290000.0*(0.0131498470948012*C1**2*C2*C23*dθ1**2+0.0131498470948012*C1**2*C2*C23*dθ2**2+0.00305810397553517*C1**2*C23**2*ddθ2+0.00305810397553517*C1**2*C23**2*ddθ3+0.0131498470948012*C1**2*C23*S2*ddθ2-0.00305810397553517*C1**2*C23*S23*dθ1**2-0.00305810397553517*C1**2*C23*S23*dθ2**2-0.00611620795107034*C1**2*C23*S23*dθ2*dθ3-0.00305810397553517*C1**2*C23*S23*dθ3**2+0.0131498470948012*C1*C2*C23*S1*ddθ1-0.00611620795107034*C1*C23**2*S1*dθ1*dθ2-0.00611620795107034*C1*C23**2*S1*dθ1*dθ3-0.0262996941896024*C1*C23*S1*S2*dθ1*dθ2-0.00305810397553517*C1*C23*S1*S23*ddθ1+1.0*S23+0.0679578661230037*ddθ3)

M = Matrix([[trigsimp(τ1.diff(ddθ1, 1)), trigsimp(τ1.diff(ddθ2, 1)), trigsimp(τ1.diff(ddθ3, 1))],
            [trigsimp(τ2.diff(ddθ1, 1)), trigsimp(τ2.diff(ddθ2, 1)), trigsimp(τ2.diff(ddθ3, 1))],
            [trigsimp(τ3.diff(ddθ1, 1)), trigsimp(τ3.diff(ddθ2, 1)), trigsimp(τ3.diff(ddθ3, 1))]])
print2(M.det())


def sub2(A):
    A = A.subs(ddθ1, 0).subs(ddθ2, 0).subs(ddθ3, 0)
    A = A.subs(dθ1, 0).subs(dθ2, 0).subs(dθ3, 0)
    A = A.subs(θ1, 0).subs(θ2, 0).subs(θ3, 0)
    return A


# print(replace2(sub2(τ1)))
# print(replace2(sub2(τ2)))
# print(replace2(sub2(τ3)))
