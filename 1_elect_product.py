# -*- coding: utf-8 -*-
"""
Spyder Editor

CVXPY code for electricity production example.

@author: Sam Davanloo

"""

import cvxpy as cp

x = cp.Variable(2, nonneg  = True) # vector variable

constraints = []
constraints.append((2/3)*x[0]+x[1]<=18)
constraints.append(2*x[0]+x[1]>=8)
constraints.append(x[0]<=12)
constraints.append(x[1]<=16)

obj_func=x[0]+x[1]

problem = cp.Problem(cp.Maximize(obj_func), constraints)

#problem.solve(solver=cp.CVXOPT,verbose = True) #verbose parameter determines showing/not showing the output
problem.solve(solver=cp.GUROBI,verbose = True)

print("obj_func =")
print(obj_func.value)
print("x =")
print(x.value)