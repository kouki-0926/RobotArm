import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.param import *

n = 150
h, a, b = np.array([ellipse2_param[0], ellipse2_param[1], 132.9])

θ = np.linspace(0, 2*np.pi, n)
x = np.linspace(cir_x0, cir_x0, n)
y = -a+a*np.cos(θ)
z = h+b*np.sin(θ)
α = np.linspace(openα, openα, n)
r0_ref = np.array([x, y, z, α]).T

simulation_3dof(r0_ref, dt, 44)
