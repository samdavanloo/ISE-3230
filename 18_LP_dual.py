#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 12:21:57 2020

@author: Sam
"""

import cvxpy as cp

#x = cp.Variable(2, nonneg = True)
x = cp.Variable(2)

obj_func = 7*x[0]+12*x[1]

constraints = []
constraints.append(0.15*x[0]+0.2*x[1]<=200) # machining time
constraints.append(0.1*x[0]+0.2*x[1]<=140) # forging time
constraints.append(2.5*x[0]+4*x[1]<=3200) # raw material
constraints.append(x[0]<=900) 
constraints.append(x[1]<=600)

constraints.append(x[0]>=0)
constraints.append(x[1]>=0)


problem = cp.Problem(cp.Maximize(obj_func), constraints)

problem.solve(solver=cp.GUROBI, verbose = True)
#problem.solve()

print("obj_func =", obj_func.value)
print("x =", x.value)

# Shadow prices or dual prices
print("optimal (0.15*x[0]+0.2*x[1]<=200) dual variable", constraints[0].dual_value)
print("optimal (0.1*x[0]+0.2*x[1]<=140) dual variable", constraints[1].dual_value)
print("optimal (2.5*x[0]+4*x[1]<=3200) dual variable", constraints[2].dual_value)
print("optimal (x[0]<=900) dual variable", constraints[3].dual_value)
print("optimal (x[1]<=600) dual variable", constraints[4].dual_value)

# Reduced costs
print("reduced cost of the 1st primal variable x[0]", (-1)*constraints[5].dual_value)
print("reduced cost of the 2nd primal variable x[1]", (-1)*constraints[6].dual_value)