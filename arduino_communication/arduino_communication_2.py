from arduino_communication import ser, move_3dof_3, destroy
import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from simulation.simulation_3dof import simulation_3dof
from simulation.逆運動学_3dof import generatOrbit_3dof


def get_val():
    value = ser.readline()
    value = value.decode()
    value = value.rstrip()
    value = value.split(",")
    value = np.array([int(value[i]) for i in range(3)])
    return value


def calc_r0ref(val):  # とりあえず z=170, α=0で固定, z,αの更新方法は今後検討
    global x, y, z
    v, threshold = np.array([3, 150])

    if(val[1] < threshold):
        x += v
    elif(val[1] > 1023-threshold):
        x -= v

    if(val[2] < threshold):
        y -= v
    elif(val[2] > 1023-threshold):
        y += v
    if(y > 0):
        y = 0
    return np.array([x, y, z, 0])


if __name__ == '__main__':
    x, y, z = np.array([150, 0, 150])
    r0_ref = np.array([x, y, z, 0])
    while True:
        try:
            next_ref = calc_r0ref(get_val())
            r0_ref = np.block([[r0_ref], [next_ref]])
            q = np.rad2deg(generatOrbit_3dof(next_ref[0:3]))
            int_q = np.round(q).astype(np.int64)
            move_3dof_3(int_q)
            print(next_ref, q, int_q)
        except KeyboardInterrupt:
            destroy()
            simulation_3dof(r0_ref[:-2, :], 0.02, 100)
            break
