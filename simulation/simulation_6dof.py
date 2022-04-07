from matplotlib import gridspec
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import csv
from simulation.逆運動学_6dof import generatOrbit_6dof
from simulation.順運動学 import q2r_6dof
from arduino_communication.arduino_communication import move_6dof


def simulation_6dof(r0_ref, filenumber):
    la, lb, lc, ld = np.array([129, 110, 150, 105])
    r01, r02, r03, r04, r05, r0E = [[], [], [], [], [], []]
    q_list = []

    num = r0_ref.shape[0]
    r0R = np.dot(np.ones((num, 1)), np.array([[0, 0, -ld]]))
    q_list = np.array([generatOrbit_6dof(r0_ref[p, :]) for p in range(num)])
    for p in range(num):
        r0, T05, T_list = q2r_6dof(q_list[p, :])
        T04 = np.dot(T05, np.linalg.inv(T_list[4]))
        T03 = np.dot(T04, np.linalg.inv(T_list[3]))
        T02 = np.dot(T03, np.linalg.inv(T_list[2]))
        T01 = np.dot(T02, np.linalg.inv(T_list[1]))
        r01.append(T01[0:3, 3])
        r02.append(T02[0:3, 3])
        r03.append(T03[0:3, 3])
        r04.append(T04[0:3, 3])
        r05.append(T05[0:3, 3])
        r0E.append(r0[0:3])
    rList = np.array([r0R, r01, r02, r03, r04, r05, r0E])

    # =================== q_list ========================
    q_list = np.round(np.rad2deg(q_list)).astype(np.int64)
    s, t = q_list.shape
    with open("csv/simulation_"+str(filenumber)+".csv", 'w') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(q_list)

# ===============================  fig  ====================================
    size = 0.85
    fig = plt.figure(figsize=(16*size, 9*size))
    spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[1.2, 2])
    # ===========================  fig1  ===================================
    ax1 = fig.add_subplot(spec[0])
    ax1.plot(np.arange(s), q_list[:, 0], label="$\\theta_1$")
    ax1.plot(np.arange(s), q_list[:, 1], label="$\\theta_2$")
    ax1.plot(np.arange(s), q_list[:, 2], label="$\\theta_3$")
    ax1.plot(np.arange(s), q_list[:, 3], label="$\\theta_4$")

    ax1.set_xlabel("step")
    ax1.set_ylabel("関節角度 [deg]")
    ax1.legend()
    ax1.grid()

    # ===========================  fig2  ===================================
    ax2 = fig.add_subplot(spec[1], projection='3d')
    ax2.plot(rList[6, :, 0], rList[6, :, 1], rList[6, :, 2], "-", color="green")

    ax2.set_xlim(-250, 250)
    ax2.set_ylim(-250, 250)
    ax2.set_zlim(-170, 170)
    ax2.set_xlabel("$x_0$")
    ax2.set_ylabel("$y_0$")
    ax2.set_zlabel("$z_0$")

    # =============== 土台生成 ===================================================
    n = 10
    α, b, h = np.array([0.8, 45, 20])
    X, Y = np.meshgrid(np.linspace(-b, b, n), np.linspace(-b, b, n))
    ax2.plot_surface(X, Y, -ld*np.ones((n, n)), alpha=α, color="black")
    ax2.plot_surface(X, Y, -(ld-h)*np.ones((n, n)), alpha=α, color="black")
    X, Z = np.meshgrid(np.linspace(-b, b, n), np.linspace(-ld, -(ld-h), 10))
    ax2.plot_surface(X, np.zeros((n, n)), Z, alpha=α, color="black")
    X, Z = np.meshgrid(np.linspace(-b, b, n), np.linspace(-(ld-h), -(ld-h)+b, n))
    ax2.plot_surface(X, b*np.ones((n, n)), Z, alpha=α, color="black")
    ax2.plot_surface(X, (b-h)*np.ones((n, n)), Z, alpha=α, color="black")
    # ===========================================================================

    ims = [ax2.plot(rList[:, i, 0], rList[:, i, 1], rList[:, i, 2], "o-", color="red") for i in range(num)]

    fig.tight_layout()
    ani = animation.ArtistAnimation(fig, ims, interval=0.001)
    ani.save("graph/simulation_"+str(filenumber)+".gif", writer='imagemagick')
    plt.show()
# ===============================  end fig  ====================================

    string = input("ready? (y/n): ")
    if(string == "y"):
        move_6dof(q_list)
