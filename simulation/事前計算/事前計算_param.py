from sympy import *

la, lb, lc, ld = symbols("la, lb, lc, ld", positive=True)
r0x, r0y, r0z = symbols("r0x, r0y, r0z", real=True)
θ1, θ2, θ3, θ4, θ5, θ6 = symbols("θ1, θ2, θ3, θ4, θ5, θ6", real=True)

parm_list_3dof = Matrix([[0, 0, 0, θ1],
                         [0, -pi/2, 0, θ2],
                         [la, 0, 0, θ3]])
r_3dof = Matrix([lb, 0, 0, 1])
r_3dof_2 = Matrix([0, lc, 0, 1])
r_3dof_3 = Matrix([lc, 0, 0, 1])

parm_list_6dof = Matrix([[0, 0, 0, θ1],
                         [0, -pi/2, 0, θ2],
                         [la, 0, 0, θ3],
                         [lb, 0, 0, θ4],
                         [0, -pi/2, 0, θ5]])
r_6dof = Matrix([0, 0, lc, 1])
