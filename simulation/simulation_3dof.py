from matplotlib import gridspec
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
import csv
from simulation.逆運動学_3dof import generatOrbit_3dof
from simulation.順運動学 import q2r_3dof
from simulation.動力学 import dynamics, dynamics_2
from simulation.可操作度 import calc_manipulability
from simulation.R2deg import R2deg
from simulation.param import ld
# from arduino_communication.arduino_communication import move_3dof


def simulation_3dof(r0_ref, dt, filenumber):
    num = r0_ref.shape[0]
    # ========== 逆運動学 =====================================================
    q_list = np.array([generatOrbit_3dof(r0_ref[p, 0:3]) for p in range(num)])
    dq_list = np.diff(q_list, axis=0, n=1)/dt
    ddq_list = np.diff(q_list, axis=0, n=2)/(dt**2)

    # ========== 順運動学 =====================================================
    T_list = np.array([q2r_3dof(q_list[p, 0:3]) for p in range(num)])
    r0R_list = np.dot(np.ones((num, 1)), np.array([[0, 0, -ld]]))
    r01_list = T_list[:, 0, 0:3, 3]
    r02_list = T_list[:, 1, 0:3, 3]
    r03_list = T_list[:, 2, 0:3, 3]
    r0E_list = T_list[:, 3, 0:3, 3]
    r_list = np.array([r0R_list, r01_list, r02_list, r03_list, r0E_list])

    # ========== 手先座標系の移動速度, 回転速度 =================================
    z01_list = T_list[:, 0, 0:3, 2]
    z02_list = T_list[:, 1, 0:3, 2]
    z03_list = T_list[:, 2, 0:3, 2]
    p0E1_list = r0E_list-r01_list
    p0E2_list = r0E_list-r02_list
    p0E3_list = r0E_list-r03_list
    Jv_list = np.array([np.block([[np.cross(z01_list[p], p0E1_list[p]), z01_list[p]],
                                  [np.cross(z02_list[p], p0E2_list[p]), z02_list[p]],
                                  [np.cross(z03_list[p], p0E3_list[p]), z03_list[p]]]).T for p in range(num)])
    v_list = np.array([np.dot(Jv_list[p], dq_list[p]) for p in range(num-1)])

    # ========== 手先座標系の姿勢 ==============---=============================
    Euler_angles_list = np.rad2deg(np.array([R2deg(T_list[p, 2, :, :]) for p in range(num)]))

    # ========== 可操作度 =====================================================
    w_list = calc_manipulability(q_list, num)

    # ========== 動力学 =======================================================
    τ_list = dynamics(dt, filenumber, dof=32)
    fn0E = np.array([np.linalg.pinv(Jv_list[p].T).dot(τ_list[:, p]) for p in range(num-2)])
    fnEE = np.array([np.block([np.dot(np.linalg.inv(T_list[p, 3, 0:3, 0:3]), fn0E[p, 0:3]),
                               np.dot(np.linalg.inv(T_list[p, 3, 0:3, 0:3]), fn0E[p, 3:6])]) for p in range(num-2)])

    JE3_T_list = dynamics_2(T_list[:, 6, :, :], num)
    J32_T_list = dynamics_2(T_list[:, 5, :, :], num)
    J21_T_list = dynamics_2(T_list[:, 4, :, :], num)

    fn33 = np.array([np.dot(JE3_T_list[p], fnEE[p]) for p in range(num-2)])
    fn22 = np.array([np.dot(J32_T_list[p], fn33[p]) for p in range(num-2)])
    fn11 = np.array([np.dot(J21_T_list[p], fn22[p]) for p in range(num-2)])
    # ========== end 動力学 ===================================================


# =============================  q_list保存  =================================
    q_list_csv = np.rad2deg(q_list)
    q_list_int = np.round(q_list_csv).astype(np.int64)
    with open("csv/simulation_"+str(filenumber)+".csv", 'w') as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerows(np.stack([q_list_csv[:, 0], q_list_csv[:, 1], q_list_csv[:, 2], r0_ref[:, 3]], 1))
    # return 0


# ===============================  fig1  ====================================
    size = 0.85
    figsize = (16*size, 9*size)  # iPhone
    # size = 3.0
    # figsize = (4*size, 3*size)  # iPad
    fig1 = plt.figure(figsize=figsize)
    spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[1.2, 2])
    t_ax1 = np.arange(0, dt*num, dt)
    fig1_title_position = -0.12
    # ===========================  sub_fig1  ===================================
    ax1 = fig1.add_subplot(spec[0])
    ax1.plot(t_ax1, q_list_int[:, 0], label="$\\theta_1$")
    ax1.plot(t_ax1, q_list_int[:, 1], label="$\\theta_2$")
    ax1.plot(t_ax1, q_list_int[:, 2], label="$\\theta_3$")
    ax1.plot(t_ax1, r0_ref[:, 3], label="$\\theta_5$")
    ax1.set_xlabel("時間 [s]")
    ax1.set_ylabel("関節角度 [deg]")
    ax1.set_xlim(0, np.max(t_ax1))
    ax1.legend()
    ax1.grid()
    ax1.set_title("図1 各関節の角度", y=fig1_title_position)

    # ===========================  sub_fig2  ===================================
    ax2 = fig1.add_subplot(spec[1], projection='3d')
    ax2.plot(r0E_list[:, 0], r0E_list[:, 1], r0E_list[:, 2], "-", color="green")
    ax2.set_xlim(-250, 250)
    ax2.set_ylim(-250, 250)
    ax2.set_zlim(-170, 170)
    ax2.set_xlabel("$x_0 [mm]$")
    ax2.set_ylabel("$y_0 [mm]$")
    ax2.set_zlabel("$z_0 [mm]$")
    ax2.set_title("図2 simulation_"+str(filenumber), y=fig1_title_position)

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
    # =============== 土台生成ここまで ===================================================

    ims = [ax2.plot(r_list[:, i, 0], r_list[:, i, 1], r_list[:, i, 2], "o-", color="red") for i in range(num)]

    fig1.tight_layout()
    plt.get_current_fig_manager().window.wm_geometry("+100+100")
    ani = animation.ArtistAnimation(fig1, ims, interval=0.001)
    ani.save("graph/simulation_"+str(filenumber)+".gif", writer='imagemagick')


# ===============================  fig2,3  ===================================
    t_0 = np.arange(0, dt*num, dt)
    t_1 = np.arange(0, dt*(num-1), dt)
    t_2 = np.arange(0, dt*(num-2), dt)
    fig_title_position = -0.25
    fig_xlim_max = np.max(t_0)


# ===============================  fig2  ===================================
    fig2 = plt.figure(figsize=figsize)
    fig2.suptitle("simulation_"+str(filenumber))
    # ===========================  sub_fig3  ===================================
    ax3 = fig2.add_subplot(241)
    ax3.plot(t_0, q_list_int[:, 0], label="$\\theta_1$")
    ax3.plot(t_0, q_list_int[:, 1], label="$\\theta_2$")
    ax3.plot(t_0, q_list_int[:, 2], label="$\\theta_3$")
    ax3.plot(t_0, r0_ref[:, 3], label="$\\theta_5$")
    ax3.set_xlabel("時間 [s]")
    ax3.set_ylabel("関節角度 [deg]")
    ax3.set_xlim(0, fig_xlim_max)
    ax3.legend()
    ax3.grid()
    ax3.set_title("図3 各関節の角度", y=fig_title_position)
    # ===========================  sub_fig4  ===================================
    ax4 = fig2.add_subplot(242)
    ax4.plot(t_1, dq_list[:, 0], label="$\dot{\\theta}_1$")
    ax4.plot(t_1, dq_list[:, 1], label="$\dot{\\theta}_2$")
    ax4.plot(t_1, dq_list[:, 2], label="$\dot{\\theta}_3$")
    ax4.set_xlabel("時間 [s]")
    ax4.set_ylabel("関節角速度 [rad/s]")
    ax4.set_xlim(0, fig_xlim_max)
    ax4.legend()
    ax4.grid()
    ax4.set_title("図4 各関節の角速度", y=fig_title_position)
    # ===========================  sub_fig5  ===================================
    ax5 = fig2.add_subplot(243)
    ax5.plot(t_2, ddq_list[:, 0], label="$\ddot{\\theta}_1$")
    ax5.plot(t_2, ddq_list[:, 1], label="$\ddot{\\theta}_2$")
    ax5.plot(t_2, ddq_list[:, 2], label="$\ddot{\\theta}_3$")
    ax5.set_xlabel("時間 [s]")
    ax5.set_ylabel("関節角加速度 $[rad/s^2]$")
    ax5.set_xlim(0, fig_xlim_max)
    ax5.legend()
    ax5.grid()
    ax5.set_title("図5 各関節の角加速度", y=fig_title_position)
    # ===========================  sub_fig6  ===================================
    ax6 = fig2.add_subplot(244)
    ax6.plot(t_0, w_list[0]*10**(-5), label="$w_1\\times 10^{-5}$")
    ax6.plot(t_0, w_list[1]*10**2, label="$w_2\\times 10^{2}$")
    ax6.plot(t_0, w_list[2]*10**0, label="$w_3$")
    ax6.plot(t_0, w_list[3]*10**0, label="$w_4$")
    ax6.set_xlabel("時間 [s]")
    ax6.set_ylabel("可操作度")
    ax6.set_xlim(0, fig_xlim_max)
    ax6.legend()
    ax6.grid()
    ax6.set_title("図6 可操作度", y=fig_title_position)
    # ===========================  sub_fig7  ===================================
    ax7 = fig2.add_subplot(245)
    ax7.plot(t_0, r_list[4, :, 0], label="$^0p_{E,x}$")
    ax7.plot(t_0, r_list[4, :, 1], label="$^0p_{E,y}$")
    ax7.plot(t_0, r_list[4, :, 2], label="$^0p_{E,z}$")
    ax7.set_xlabel("時間 [s]")
    ax7.set_ylabel("位置 [mm]")
    ax7.set_xlim(0, fig_xlim_max)
    ax7.legend()
    ax7.grid()
    ax7.set_title("図7 手先座標系の位置", y=fig_title_position)
    # ===========================  sub_fig8  ===================================
    ax8 = fig2.add_subplot(246)
    ax8.plot(t_1, v_list[:, 0], label="$^0\dot{p}_{E,x}$")
    ax8.plot(t_1, v_list[:, 1], label="$^0\dot{p}_{E,y}$")
    ax8.plot(t_1, v_list[:, 2], label="$^0\dot{p}_{E,z}$")
    ax8.set_xlabel("時間 [s]")
    ax8.set_ylabel("速度 [mm/s]")
    ax8.set_xlim(0, fig_xlim_max)
    ax8.legend()
    ax8.grid()
    ax8.set_title("図8 手先座標系の移動速度", y=fig_title_position)
    # ===========================  sub_fig9  ===================================
    ax9 = fig2.add_subplot(247)
    ax9.plot(t_0, Euler_angles_list[:, 0], label="$\phi$")
    ax9.plot(t_0, Euler_angles_list[:, 1], label="$\\theta$")
    ax9.plot(t_0, Euler_angles_list[:, 2], label="$\psi$")
    ax9.set_xlabel("時間 [s]")
    ax9.set_ylabel("オイラー角 [deg]")
    ax9.set_xlim(0, fig_xlim_max)
    ax9.legend()
    ax9.grid()
    ax9.set_title("図9 手先座標系の姿勢", y=fig_title_position)
    # ===========================  sub_fig10  ===================================
    ax10 = fig2.add_subplot(248)
    ax10.plot(t_1, v_list[:, 3], label="$^0\omega_{E,x}$")
    ax10.plot(t_1, v_list[:, 4], label="$^0\omega_{E,y}$")
    ax10.plot(t_1, v_list[:, 5], label="$^0\omega_{E,z}$")
    ax10.set_xlabel("時間 [s]")
    ax10.set_ylabel("角速度 [rad/s]")
    ax10.set_xlim(0, fig_xlim_max)
    ax10.legend()
    ax10.grid()
    ax10.set_title("図10 手先座標系の回転速度", y=fig_title_position)

    fig2.tight_layout()
    plt.get_current_fig_manager().window.wm_geometry("+50+50")
    fig2.savefig("graph/simulation_"+str(filenumber)+".png")


# ===============================  fig3  ===================================
    fig3 = plt.figure(figsize=figsize)
    torque_max1456 = 1.30723311
    torque_max23 = 2.059407
    fig3.suptitle("simulation_"+str(filenumber)+"_2")
    # ===========================  sub_fig11  ===================================
    ax11 = fig3.add_subplot(231)
    ax11.plot(t_2, τ_list[0]/(10**9), label="$\\tau_1$")
    ax11.plot(t_2, τ_list[1]/(10**9), label="$\\tau_2$")
    ax11.plot(t_2, τ_list[2]/(10**9), label="$\\tau_3$")
    ax11.hlines(torque_max1456, 0, fig_xlim_max, color="red", label="サーボモータ1456最大 $\pm"+str(torque_max1456)+" Nm$")
    ax11.hlines(-torque_max1456, 0, fig_xlim_max, color="red")
    ax11.hlines(torque_max23, 0, fig_xlim_max, color="tomato", label="サーボモータ23最大 $\pm"+str(torque_max23)+" Nm$")
    ax11.hlines(-torque_max23, 0, fig_xlim_max, color="tomato")
    ax11.set_xlabel("時間 [s]")
    ax11.set_ylabel("関節トルク $[Nm]$")
    ax11.set_xlim(0, fig_xlim_max)
    ax11.legend()
    ax11.grid()
    ax11.set_title("図11 各サーボモータのトルク", y=fig_title_position)
    # ===========================  sub_fig12  ===================================
    ax12 = fig3.add_subplot(232)
    ax12.plot(t_2, fnEE[:, 0]/(10**6), label="$^Ef_{E,x}$")
    ax12.plot(t_2, fnEE[:, 1]/(10**6), label="$^Ef_{E,y}$")
    ax12.plot(t_2, fnEE[:, 2]/(10**6), label="$^Ef_{E,z}$")
    ax12.plot(t_2, fn33[:, 0]/(10**6), label="$^3f_{3,x}$")
    ax12.plot(t_2, fn33[:, 1]/(10**6), label="$^3f_{3,y}$")
    ax12.plot(t_2, fn33[:, 2]/(10**6), label="$^3f_{3,z}$")
    ax12.plot(t_2, fn22[:, 0]/(10**6), label="$^2f_{2,x}$")
    ax12.plot(t_2, fn22[:, 1]/(10**6), label="$^2f_{2,y}$")
    ax12.plot(t_2, fn22[:, 2]/(10**6), label="$^2f_{2,z}$")
    ax12.plot(t_2, fn11[:, 0]/(10**6), label="$^1f_{1,x}$")
    ax12.plot(t_2, fn11[:, 1]/(10**6), label="$^1f_{1,y}$")
    ax12.plot(t_2, fn11[:, 2]/(10**6), label="$^1f_{1,z}$")
    ax12.set_xlabel("時間 [s]")
    ax12.set_ylabel("手先, 各モータに発生する力 $[N]$")
    ax12.set_xlim(0, fig_xlim_max)
    ax12.legend()
    ax12.grid()
    ax12.set_title("図12 手先, 各モータに発生する力", y=fig_title_position)
    # ===========================  sub_fig13  ===================================
    ax13 = fig3.add_subplot(233)
    ax13.plot(t_2, fnEE[:, 3]/(10**9), label="$^En_{E,x}$")
    ax13.plot(t_2, fnEE[:, 4]/(10**9), label="$^En_{E,y}$")
    ax13.plot(t_2, fnEE[:, 5]/(10**9), label="$^En_{E,z}$")
    ax13.plot(t_2, fn33[:, 3]/(10**9), label="$^3n_{3,x}$")
    ax13.plot(t_2, fn33[:, 4]/(10**9), label="$^3n_{3,y}$")
    ax13.plot(t_2, fn33[:, 5]/(10**9), label="$^3n_{3,z}$")
    ax13.plot(t_2, fn22[:, 3]/(10**9), label="$^2n_{2,x}$")
    ax13.plot(t_2, fn22[:, 4]/(10**9), label="$^2n_{2,y}$")
    ax13.plot(t_2, fn22[:, 5]/(10**9), label="$^2n_{2,z}$")
    ax13.plot(t_2, fn11[:, 3]/(10**9), label="$^1n_{1,x}$")
    ax13.plot(t_2, fn11[:, 4]/(10**9), label="$^1n_{1,y}$")
    ax13.plot(t_2, fn11[:, 5]/(10**9), label="$^1n_{1,z}$")
    ax13.set_xlabel("時間 [s]")
    ax13.set_ylabel("手先, 各モータに発生するモーメント $[Nm]$")
    ax13.set_xlim(0, fig_xlim_max)
    ax13.legend()
    ax13.grid()
    ax13.set_title("図13 手先, 各モータに発生するモーメント", y=fig_title_position)

    fig3.tight_layout()
    plt.get_current_fig_manager().window.wm_geometry("+0+0")
    fig3.savefig("graph/simulation_"+str(filenumber)+"_2.png")
# ===============================  end fig3  ===================================
    # plt.show()
# ===============================  end fig  ====================================

    # string = input("ready? (y/n): ")
    # if(string == "y"):
    #     move_3dof(q_list_int)
