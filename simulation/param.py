import numpy as np

la, lb, lc, ld = np.array([129, 110, 150, 105])

dt = 0.01

openα, closeα = np.array([0, 65])
hand_open, hand_close = np.array([0, 1])

cir_x0 = 93
cir_param = np.array([50, 125, 125])  # 43
ellipse_param = np.array([60, 31, 160])  # 45
ellipse2_param = np.array([50, 87.5, 132.5])  # 44
