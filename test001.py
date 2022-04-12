from simulation.軌道生成 import calc_a2
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib


def main(ξ, t, Δ):
    ξim1, ξi, ξip1 = ξ
    tim1, ti, tip1 = t
    num = 30

    t1 = np.linspace(0, 2*Δ, num)
    t2 = np.linspace(tim1+2*Δ, ti-2*Δ, num)
    t3 = np.linspace(0, 2*Δ, num)
    t4 = np.linspace(0, 2*Δ, num)
    t5 = np.linspace(ti+2*Δ, tip1-2*Δ, num)
    t6 = np.linspace(0, 2*Δ, num)
    T = np.block([t1,
                  t2,
                  t3+ti-2*Δ,
                  t4+ti,
                  t5,
                  t6+tip1-2*Δ])

    Bim1 = (ξi-ξim1)/(ti-tim1)
    Bip1 = (ξip1-ξi)/(tip1-ti)

    a = ξi-Bim1*Δ
    b = ξi+Bip1*Δ
    c = ξi-Bip1*Δ
    d = ξi+Bim1*Δ

    Aim1 = ((1/2)*(a+b)-ξim1)/(ti-tim1-2*Δ)
    Ai = (1/(4*Δ))*((c+d)-(a+b))
    Aip1 = (ξip1-(1/2)*(c+d))/(tip1-ti-2*Δ)

    ξ1 = calc_a2(ξim1, 0, 0,
                 Aim1*Δ+ξim1, Aim1, 0,
                 2*Δ, t1)

    ξ2 = Aim1*(t2-(tim1+Δ))+ξim1

    ξ3 = calc_a2((1/2)*(a+b)-Aim1*Δ, Aim1, 0,
                 ξi, Ai, 0,
                 2*Δ, t3)

    ξ4 = calc_a2(ξi, Ai, 0,
                 (1/2)*(c+d)+Aip1*Δ, Aip1, 0,
                 2*Δ, t4)

    ξ5 = Aip1*(t5-(tip1-Δ))+ξip1

    ξ6 = calc_a2(ξip1-Aip1*Δ, Aip1, 0,
                 ξip1, 0, 0,
                 2*Δ, t6)

    ξ = np.block([ξ1, ξ2, ξ3, ξ4, ξ5, ξ6])
    return [ξ, T]


def draw_fig(ξ, T, file_num):
    fig = plt.figure(figsize=(16*0.8, 9*0.8))
    fig.suptitle("test001")

    ax = fig.add_subplot(111)
    ax.plot(T, ξ, label="$\\xi$")
    ax.set_xlabel("時間 [s]")
    ax.set_ylabel("\\xi []")
    ax.set_xlim(0, np.max(t))
    ax.set_ylim(np.min(ξ)-30, np.max(ξ)+30)
    ax.legend()
    ax.grid()
    ax.set_title("図1 test001", y=-0.15)

    fig.tight_layout()
    fig.savefig("graph/test/test"+str(file_num)+".png")
    plt.show()


if __name__ == '__main__':
    ξ = np.array([0, 50, 20])
    t = np.array([0, 1, 3])
    Δ = 0.20
    ξ, T = main(ξ, t, Δ)
    draw_fig(ξ, T, "001")
