import serial
import time


baudRate = 115200
# baudRate = 38400
# baudRate = 9600

try:
    ser = serial.Serial("COM3", baudRate)
    time.sleep(2)
    print("Open Port")
except:
    print("arduinoの接続を確認してください")


def send(pin, val):
    if(pin == 3):
        val = str(val)+'a'
    elif(pin == 5):
        val = str(val)+'b'
    elif(pin == 6):
        val = str(val)+'c'
    elif(pin == 9):
        val = str(val)+'d'
    elif(pin == 10):
        val = str(val)+'e'
    elif(pin == 11):
        val = str(val)+'f'
    ser.write(bytes(val, 'utf-8'))


def destroy():
    ser.close()
    print("Close Port")


def move_3dof(q_list):
    num = q_list.shape[0]
    for i in range(num):
        send(3, q_list[i, 0])
        send(5, q_list[i, 1])
        send(6, q_list[i, 2])
        time.sleep(0.01)
    destroy()


def move_3dof_2(q_list):
    num = q_list.shape[0]
    for i in range(num):
        send(3, q_list[i, 0])
        send(5, q_list[i, 1])
        send(6, q_list[i, 2])
        send(9, q_list[i, 3])
        time.sleep(0.01)
    destroy()


def move_3dof_3(q):
    send(3, q[0])
    send(5, q[1])
    send(6, q[2])
    send(9, 0)
    time.sleep(0.01)


def move_6dof(q_list):
    num = q_list.shape[0]
    for i in range(num):
        send(3, q_list[i, 0])
        send(5, q_list[i, 1])
        send(6, q_list[i, 2])
        send(9, q_list[i, 3])
        time.sleep(0.01)
