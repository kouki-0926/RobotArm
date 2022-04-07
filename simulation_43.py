import numpy as np
from simulation.simulation_3dof import simulation_3dof
from simulation.param import *

n = 300
h, r = cir_param[0:2]

θ = np.linspace(0, 2*np.pi, n)
x = np.linspace(cir_x0, cir_x0, n)
y = -r+r*np.cos(θ)
z = h+r*np.sin(θ)
α = np.linspace(openα, openα, n)
r0_ref = np.array([x, y, z, α]).T

simulation_3dof(r0_ref, dt, 43)
