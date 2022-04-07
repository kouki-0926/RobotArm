import numpy as np
import csv
import sys
from arduino_communication.arduino_communication import move_3dof, move_3dof_2

# ======================================================================
# arduino_communication.ino の MANUAL をコメントアウトしているかを確認せよ
# ======================================================================


def main(filenumber, repeat_N):
    with open("csv/simulation_"+str(filenumber)+".csv") as f:
        reader = csv.reader(f)
        l = [row for row in reader]
        q_list = np.array([[float(v) for v in row] for row in l])
        q_list = np.round(q_list).astype(np.int64)
        n = q_list.shape[1]
        if(n == 3):
            move_3dof(np.tile(q_list, (int(repeat_N), 1)))
        elif(n == 4):
            move_3dof_2(np.tile(q_list, (int(repeat_N), 1)))


if __name__ == '__main__':
    try:
        file_num = sys.argv[1]
    except:
        print("Error: param doesn't exist. file_num = 48")
        file_num = 48
    try:
        repeat_n = sys.argv[2]
    except:
        print("Error: param doesn't exist. repeat_n = 1")
        repeat_n = 1
    main(file_num, repeat_n)
